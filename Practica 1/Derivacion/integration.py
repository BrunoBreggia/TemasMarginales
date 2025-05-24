# integracion por metodo trapezoidal
import numpy as np
import matplotlib.pyplot as plt

def integrar(a, b, func, res=1000):
    test_pts = np.linspace(a,b,res)
    step = (b-a)/res
    value = 0.5*step*(func(a)+func(b))  # initial value
    for i in test_pts[1:-2]:
        value += step*func(i)
    return value

def function1(num):
    if num < 0:
        raise ValueError
    elif num == 0:
        return 0
    else:
        return np.arctan(num)*np.log(num)

def function2(num):
    if num < 0 or num > 1:
        raise ValueError
    elif num == 0 or num==1:
        return 0
    else:
        return np.arctanh(num)*np.log(num)

def graph(a,b,func,res=1000):
    test_pts = np.linspace(a, b, res)
    values = []
    for i in test_pts:
        values.append(func(i))
    plt.plot(test_pts, values)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # graph(0,1,function1)
    value = integrar(0,1,function1, res=50_000)
    print(f"El resultado (aproximado) de la integral es {value}")
    calculated = np.pi**2/48 - np.pi/4 + 0.5*np.log(2)
    # calculated = np.pi ** 2 / 24 - np.log(2)
    print(f"Este es el valor calculado a mano:{calculated}")
    print(f"Diferencia de la estimacion: {abs(value-calculated)}")

