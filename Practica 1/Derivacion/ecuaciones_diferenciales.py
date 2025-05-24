import matplotlib.pyplot as plt

# Funcion Logistica

def memoization(func):
    calls = {}
    def memoized(*args):
        if args not in calls.keys():
            calls[args] = func(*args)
        return calls[args]
    return memoized

# funcion recursiva
@memoization
def logistico(n, x0):
    if n == 1:
        return x0
    return 4*logistico(n-1, x0)*(1-logistico(n-1, x0)/45e3)



if __name__ == "__main__":
    # print(logistico(200, 0.05))

    # Metodo de Euler para Crecimiento poblacional
    dN_dt = lambda N,r,A: r*N*(1-N/A)

    poblacion = [5]  # condicion inicial en t=0
    r = 4  # tasa de crecimiento
    A = 2000  # capacidad
    paso = 0.2
    for i in range(1,20):
        poblacion.append(poblacion[-1]+paso*dN_dt(poblacion[-1],r,A))
    plt.plot(poblacion)
    plt.grid()
    plt.title("Crecimiento poblacional normalizado")
    plt.show()

    # Metodo de Euler para oscilador armonico
    d2x_dt2 = lambda A, x: -A*x
    posicion = [0]
    velocidad = [25]
    paso = 0.01
    A = 2

    for i in range(1,800):
        vel = velocidad[-1] + paso*d2x_dt2(A,posicion[-1])
        pos = posicion[-1] + paso*velocidad[-1]

        posicion.append(pos)
        velocidad.append(vel)

    plt.plot(posicion, label="posicion")
    plt.plot(velocidad, label="velocidad")
    plt.grid()
    plt.title("Oscilador armonico")
    plt.show()