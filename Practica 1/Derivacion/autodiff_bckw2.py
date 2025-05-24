import numpy as np

class Nodo:
    def __init__(self, val):
        self.val = val
        self.adj = 0
        self.operacion = "input"
        self.pullback_fn = None
        self.padres = []

    def __add__(self, other):
        res = Nodo(self.val + other.val)

        # derivadas parciales
        der_1 = 1
        der_2 = 1

        # agrego nodos padres
        res.padres.extend([(self, der_1),
                           (other, der_2)])
        res.operacion = "add"

        return res

    def __mul__(self, other):
        res = Nodo(self.val * other.val)

        # derivadas parciales
        der_1 = other.val
        der_2 = self.val

        # agrego nodos padres
        res.padres.extend([(self, der_1),
                           (other, der_2)])
        res.operacion = "mul"

        return res

    def __str__(self):
        return f"Nodo con valor {self.val}, operacion={self.operacion}"

    def backward(self, begin=True):
        if begin: self.adj = 1
        for nodo, der in self.padres:
            nodo.adj += self.adj * der
            nodo.backward(begin=False)

    def grad(self):
        return self.adj

if __name__ == "__main__":
    x = Nodo(2.)
    y = Nodo(3.)
    z = Nodo(4.)
    w = Nodo(5.)

    c_1 = Nodo(-1)
    c2 = Nodo(2)

    v1 = c_1*z
    v2 = x*x
    v3 = c2*w
    v4 = v1*v2
    v5 = y*v3
    v6 = v4 + v5

    v6.backward()
    print(f"{v6.val}")

    print(f"{x.adj=}")
    print(f"{y.adj=}")
    print(f"{z.adj=}")
    print(f"{w.adj=}")

