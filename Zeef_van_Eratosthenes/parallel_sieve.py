# coding=utf-8
"""
De stappen die in het verslag 'Zeef_van_Eratosthenes_verslag.pdf' 
staan moeten nu parallell geschreven worden. 

1 De getallen van 2 t/m 15 worden wederom opgeschreven
  1.1 per thread wordt er een getal opgeschreven, de threads zijn niet afhankelijk van elkaar

2 Er is geen parallelle methode nodig om het kleinste getal in de lijst te omcirkelen

3 Voor elk getal groter dan het omcirkelde getal; als het getal een meervoud is van het 
  omcirkelde getal, markeer het. 
  3.1 Deze stap kan geparalleliseerd worden. 
      Een thread die een meervoud markeert, is niet afhankelijk van een andere thread
      die een ander meervoud markeert. 
  3.2 threads markeren de meervouden van het grootste omcirkelde getal 

4 Terug gaan naar stap 2 om vervolgens de stappen weer te herhalen kunnen ook niet geparallelliseerd
  worden. Dit omdat stap 2 ook niet parallell loopt. 

compile: mpirun -n 4 --oversubscribe python3 parallel_sieve.py
"""
from mpi4py import MPI
import time

start_time = time.time() # start time tracking

# MPI Variables
comm = MPI.COMM_WORLD   # communicator object
rank = comm.Get_rank()  # return rank of this process in a communicator    id
size = comm.Get_size()  # return number of processes in a communicator     numprocesses
# print('Process {} out of {}'.format(rank,size))

start_num = (rank * 2) + 1 
maximum = 1000000

priem = [] # list with all the prime numbers 

# Loop through the numbers
for i in range(start_num, maximum, size * 2):
    true_prime = True
    for div_number in range(2, i):
        if i % div_number == 0:
            true_prime = False
            break
    if true_prime:
        priem.append(i)

# Gather works by specifying what you're gathering, and where the data will go (root), in this case the master worker
results = comm.gather(priem, root=0)

# The master worker
if rank == 0:
    total_time = round(time.time() - start_time, 5) # Total elapsed time

    print('Found prime numbers up to: ' + str(maximum))
    print('Total processes: ' + str(size))
    print("Algorithm took: {:.5f} second(s)".format(total_time))
    
    # Each process found their own prime numbers, now we need to merge them together 
    # so we can view all of the prime numbers found
    merged_priem = [item for sublist in results for item in sublist]
    merged_priem.sort()
    print('Amount of primes found: ' + str(len(merged_priem)))