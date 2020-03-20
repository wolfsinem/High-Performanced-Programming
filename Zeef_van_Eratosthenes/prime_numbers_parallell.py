# coding=utf-8
"""
compile for mp: mpiexec -n 1 python3 prime_numbers.py
"""

import time
from mpi4py import MPI 

# variabelen voor scattering
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start_time = time.time()

def priemgetal(maximum):
    priem = [] # array met alle priemgetallen vanaf 2 t/m een maximum
    count = 0 # totaal aantal priemgetallen
    k = 2 

    for i in range(k, maximum):
        priem.append(i)

    # Loop door de lijst 
    for j in priem:
        count += 1
        for i in priem:
            if i % j == 0:
                if i != j:
                    priem.remove(i)
    return count

count = priemgetal(1000000)
total_time = time.time() - start_time

print("Totaal: {}".format(count))
print("Sequential algorithm took: {:.5f} second(s)".format(total_time))
