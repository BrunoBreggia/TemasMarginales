import RNA
from time import time

rna = "AGCACACAGGC"
# rna = "AACCGGGUCAGGUCCGGAAGGAAGCAGCCCUAA"
## CIUDADO con usar esta ultima secuencia
# rna = "CCACGGCGACUAUAUCCCUGGUGUUCACCUCUUCCCAUUCCGAACAGAGUCGUUAAGCCCAGGAGAGCCGAUGGUACUGCUUUAUUGCGGGAGAGUAGGUCGUCGCCGAGU"

A,G,C,U = 'A G C U'.split(' ')
bond_energies = {
    (G,C): -3,
    (C,G): -3,
    (A,U): -2,
    (U,A): -2,
    (G,U): -1,
    (U,G): -1,
}

def nussinov_fold(sequence):
    """
    Algoritmo de Nussinov.
    Resuelve la estructura de minima energía libre de una secuencia de ARN
    con las siguientes suposiciones:

    * La energía de los enlaces son siempre constantes e iguales a:\n
        - E(G,C) = -3\n
        - E(A,U) = -2\n
        - E(G,U) = -1

    * No se tienen en cuenta pseudonudos

    * No se permiten emparejamientos de bases a una distancia menor a 4

    :param sequence: string de letras A,G,U,C
    :return: energia de la estructura de minima energia libre y la estructura
    de la misma en formato punto-paréntesis
    """

    # Caso base
    if len(sequence) <= 3:
        return 0, "."*len(sequence)

    # CASO 1: la primer base no forma ningun emparejamiento
    e, s = nussinov_fold(sequence[1:]) # llamada recursiva a la porcion restante
    s = "." + s # una base sin emparejar se representa con un punto
    alternatives = [(e, s)]  # lista de estructuras posibles (y sus energias)

    # CASO 2: la primer base forma enlace con un nucleotido dentro de la secuencia
    # Se prueban todos los casos posibles con un bucle
    for k in range(4,len(sequence)):

        # se obtiene la energia libre del emparejamiento
        e_bond = bond_energies.get((sequence[0],sequence[k]), 0)

        # si el emparejamiento no es posible se saltea esta iteracion
        if e_bond == 0:
            continue

        # llamadas recursivas para las mitades resultantes
        e_seq_1, s_seq_1 = nussinov_fold(sequence[1:k])
        e_seq_2, s_seq_2 = nussinov_fold(sequence[k+1:])

        # se calcula la energia total para este caso (y se arma su estructura)
        e = e_seq_1 + e_bond + e_seq_2
        s = "(" + s_seq_1 + ")" + s_seq_2

        # agrego la alternativa halladas a la lista de estructuras posibles
        alternatives.append( (e,s) )

    # se ordenan las configuraciones posibles segun su energia libre (ascendente)
    alternatives.sort(key=lambda x: x[0])

    # retornamos la estructura de menor energia
    return alternatives[0]


if __name__ == "__main__":

    # descomentar arriba la secuencia target deseada
    energy, structure = nussinov_fold(rna)
    print(f"{energy=}")
    print(f"{structure=}")

    # # Analisis de complejidad
    # with open("time_analysis_nussinov.txt", 'w') as file:
    #     for i in range(len(rna)):
    #         inicio = time()
    #         energy, structure = nussinov_fold(rna[:i])
    #         fin = time()
    #         print(f"Longitud: {i}", file=file)
    #         print(f"{energy=}", file=file)
    #         print(f"{structure=}", file=file)
    #         print(f"Duracion: {fin-inicio}", file=file)
    #         print("-------------------", file=file)
    #         if fin-inicio > 60*3:  # si se demora más de tres minutos corto el bucle de prueba
    #             break

    # RNA.plot_structure("rna_structure.ps", rna, structure)

