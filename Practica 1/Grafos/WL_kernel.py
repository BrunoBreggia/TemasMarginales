# Weisfeiler-Lehman Kernel
from functools import total_ordering
from os.path import exists

grafoA = [ # tiene 6 nodos
    (1,2), (1,3),
    (2,1), (2,3), (2,4),
    (3,1), (3,2), (3,4), (3,5), (3,6),
    (4,2), (4,3),
    (5,3),
    (6,3)
]

grafoB = [ # tiene 6 nodos
    (1,2), (1,3),
    (2,1), (2,3),
    (3,1), (3,2), (3,4), (3,5),
    (4,2), (4,3), (4,6),
    (5,3),
    (6,4)
]

class Nodo:

    total_counter = 0
    existent_hashes = {}
    hash_counter = {}

    def __init__(self):
        self.hs_vecinos = []
        self.hash = 1

    def add_neighbour(self, other):
        self.hs_vecinos.append(other.hash)

    def empty_neighbours(self):
        self.hs_vecinos = []

    def update_hash(self):
        # call only once after updating node in an iteration
        self.hs_vecinos.append(self.hash)
        hs = tuple(sorted(self.hs_vecinos))
        if hs not in self.existent_hashes.keys():
            Nodo.total_counter += 1
            self.existent_hashes[hs] = Nodo.total_counter

        self.hash = self.existent_hashes[hs]
        print(f"Hash assigned to {hs} : {self.hash}")
        if self.hash not in self.hash_counter.keys():
            self.hash_counter[self.hash] = 1
        else:
            self.hash_counter[self.hash] += 1


    # def __hash__(self):
    #     hs = tuple(sorted(self.hs_vecinos))
    #     if hs not in self.existent_hashes.keys():
    #         Nodo.total_counter += 1
    #         self.existent_hashes[hs] = Nodo.total_counter


    @classmethod
    def wl_kernel(cls):
        kernel = [cls.hash_counter[i] for i in range(1,cls.total_counter+1)]
        return kernel

    @classmethod
    def reset_hash_counter(cls):
        cls.hash_counter = {}

    @classmethod
    def reset_hashing_process(cls):
        cls.total_counter = 0
        cls.existent_hashes = {}
        cls.hash_counter = {}


if __name__ == "__main__":

    grafo = grafoA
    n_nodos = 6

    nodos = [Nodo() for _ in range(n_nodos)]

    for n in nodos:
        n.update_hash()

    for i in range(3):

        # print("--------------")
        for origen, destino in grafo:
            # print(origen, "->", destino)
            nodos[origen-1].add_neighbour(nodos[destino-1])

        for n in nodos:
            n.update_hash()
            n.empty_neighbours()

    # print para ver hashes
    for hs in Nodo.hash_counter:
        print(hs, Nodo.hash_counter[hs])

