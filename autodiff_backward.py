import numpy as np

# video: https://www.youtube.com/watch?v=1dqoFhl3zQQ

grafo_computacional = [
    ("inp", (0,)),  # 0
    ("inp", (1,)),  # 1
    ("log", (0,)),  # 2
    ("mul", (0,1)), # 3
    ("sin", (1,)),  # 4
    ("add", (2,3)), # 5
    ("sub", (5,4)), # 6
]

fn_library = {
    "inp": lambda x: x ,
    "add": lambda x, y: x+y ,
    "mul": lambda x, y: x*y ,
    "sub": lambda x, y: x-y ,
    "log": lambda x: np.log(x) ,
    "sin": lambda x: np.sin(x) ,
}

# solo computa el valor resultante, sin derivadas
def computar_grafo(grafo, inputs):
  values = list(inputs)
  for operation, indeces in grafo:
    if operation == "inp":
      continue
    args = [values[index] for index in indeces]
    result = fn_library[operation](*args)
    values.append(result)
  return values[-1]

sample_input = (3,5)
valor = computar_grafo(grafo_computacional, sample_input)
print(f"El resultado d ela operacion es {valor}")

# reglas de backprop
def inp_backprop_rule(x):
  z = x

  def inp_pullback(z_adjoint):
    x_adjoint = z_adjoint
    return (x_adjoint, )

  return z, inp_pullback

def add_backprop_rule(x, y):
  z = x + y

  def add_pullback(z_adjoint):
    x_adjoint = z_adjoint
    y_adjoint = z_adjoint
    return (x_adjoint, y_adjoint)

  return z, add_pullback

def sub_backprop_rule(x, y):
  z = x - y

  def sub_pullback(z_adjoint):
    x_adjoint = z_adjoint
    y_adjoint = -z_adjoint
    return (x_adjoint, y_adjoint)

  return z, sub_pullback

def mul_backprop_rule(x, y):
  z = x * y

  def mul_pullback(z_adjoint):
    x_adjoint = y*z_adjoint
    y_adjoint = x*z_adjoint
    return (x_adjoint, y_adjoint)

  return z, mul_pullback

def sin_backprop_rule(x):
  z = np.sin(x)

  def sin_pullback(z_adjoint):
    x_adjoint = np.cos(x)*z_adjoint
    return (x_adjoint, )

  return z, sin_pullback

def log_backprop_rule(x):
  z = np.log(x)

  def log_pullback(z_adjoint):
    x_adjoint = z_adjoint/x
    return (x_adjoint, )

  return z, log_pullback

# backpropagation library
backprop_library = {
    "inp" : inp_backprop_rule,
    "add" : add_backprop_rule,
    "sub" : sub_backprop_rule,
    "mul" : mul_backprop_rule,
    "sin" : sin_backprop_rule,
    "log" : log_backprop_rule,
}

# vector jacobian product
def vjp(grafo, inputs):
  """vector jacobian product"""
  values = list(inputs)
  pullback_stack = []

  # forward pass
  for operation, indices in grafo:
    if operation == "inp":
      continue
    args = [values[index] for index in indices]
    result, pullback_func = backprop_library[operation](*args)
    values.append(result)
    pullback_stack.append((pullback_func, indices))

  # backward pass (evaluation function)
  def pullback(output_adjoint):
    adjoint_values = np.zeros(len(values))
    adjoint_values[-1] = output_adjoint

    for i, (pullback_func, indices) in enumerate(reversed(pullback_stack)):
      current_adjoint_value = adjoint_values[-i-1]
      adjoint_args = pullback_func(current_adjoint_value)

      for index, adjoint in zip(indices, adjoint_args):
        adjoint_values[index] += adjoint

    return adjoint_values[:len(inputs)]

  return values[-1], pullback

sample_input = (3,5)
resultado, pullback_fn = vjp(grafo_computacional, sample_input)
print(f"El resultado de la operacion es {resultado}")
print(f"El gradiente en este punto es\n{pullback_fn(1.0)}")
