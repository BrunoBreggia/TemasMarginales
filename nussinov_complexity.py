import matplotlib.pyplot as plt

tiempos = []

with open("Matematica/time_analysis_nussinov.txt", "r") as file:
    for line in file:
        if "Duracion: " == line[:10]:
            tiempos.append(float(line[10:].strip('\n')))

longitudes = list(range(len(tiempos)))
plt.scatter(longitudes, tiempos)

for i, label in enumerate(longitudes):
    plt.annotate(str(label), (longitudes[i], tiempos[i])) #, textcoords="offset points", xytext=(0,5), ha='center')

plt.grid()
# plt.legend()
plt.xlabel("Lingitud de secuencia")
plt.ylabel("Tiempo en segundos")
plt.title("Complejidad temporal de Nussinov")
plt.show()

