import matplotlib.pyplot as plt
import numpy as np

def derivada(func, x, paso=1e-5):
    df = func(x+paso)-func(x)
    return df/paso

if __name__ == "__main__":
    func = lambda x: 50*np.exp(-x/10)*np.sin(x)

    tiempo = np.linspace(0,40,200)
    funcion = func(tiempo)
    funcion_prima = [derivada(func,t) for t in tiempo]

    plt.plot(funcion, label="funcion original")
    plt.plot(funcion_prima, label="funcion derivada")

    plt.grid()
    plt.show()

