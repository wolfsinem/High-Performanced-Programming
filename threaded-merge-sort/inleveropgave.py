from timeit import default_timer as timer
import threading, logging
from random import randint
from typing import List
import multiprocessing
import numpy as np 
import math


"""
Merge sort is een efficient sorteeralgoritme. Dit algoritme neemt een array, 
spltst deze in (bijna) twee gelijke sub-lijsten om het vervolgens te gaan
soreren en samen te voegen tot een nieuwe gesorteerde array. De complexiteit
vandit sorteeralgortime zit in het samenvoegen. 

Stel er zijn twee gesorteerde sub-lijsten:
lijt_1 =  14,  30,  34,  56,  77
lijt_2 =  15,  20,  51,  52,  93

Het kleinste element wordt telkens genomen van de twee sub-lijsten nadat de indexen met
elkaar worden vergeleken. Getallen 14 en 15 worden met elkaar vergeleken. Welk getal is kleiner? 
Die komt als eerst in de nieuwe array. 14 > 15 -> 20 -> 30 -> 34 -> 51 -> 52 -> 77 -> 93 
"""

def generate_array(size=8,max=20):
    """Create an array of lenght 'size' containing random numbers from the range 0 up to 'max' """
    return [randint(0,max) for _ in range(size)]


def merge_sort(lijst: List[int]):
    """
    Implementation of the Merge Sort Algortihm.
    Check threaded_merge_sort.png in folder "visuals" for further visual explanation.
    This algorithm will be used for a new function with processes.
    """
    if len(lijst) <=1: 
        return lijst

    left = merge_sort(lijst[:len(lijst) // 2 ])
    right = merge_sort(lijst[len(lijst) // 2:])

    return merge(left,right)


def merge(left: int, right: int):
    """Merge the sublists"""
    lijst = []
    
    l=0
    r=0
    
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            lijst.append(left[l])
            l += 1
        else:
            lijst.append(right[r])
            r += 1
    if l == len(left):
        lijst.extend(right[r:])
    else:
        lijst.extend(left[l:])
    
    return lijst


def split_for_threading(lijst: List[int], processes: int):
    """
    Param_ lijst: generated list with x integers
    Param processes: number of processes being used
    Var split: divides the list by the amount of processes 
    """
    split = int(math.ceil(float(len(lijst)) / processes))
    splitted_list = [lijst[i * split:(i + 1) * split] for i in range(processes)]
    
    return splitted_list


def parallel_merge_sort(lijst: List[int], processes: int):
    """
    The pool object offers parallelization of the merge sort
    function. 
    """
    pool = multiprocessing.Pool(processes=processes)
    splitted_list = split_for_threading(lijst,processes)
    
    lijst = pool.map(merge_sort, splitted_list)

    while len(lijst) > 1:

        if len(lijst) % 2 == 1:
            extra = lijst.pop() 
        else: None

        for i in range(0, len(lijst), 2):
            lijst = (lijst[i], lijst[i + 1])
        
        lijst = pool.map(merge,lijst) + ([extra] if extra else [])

    return lijst[0]


def set_time(function,list_):
    """function that can be used for each algorithm to measure the execution time"""
    for i in list_:
        start_time = timeit.default_timer()
        function(i)
        print('This algorithm took {:.4f} seconds'.format((timeit.default_timer() - start_time)))

if __name__ == "__main__":
    print("Multiprocessed Merge Sort Algorithm")
    process_amount = multiprocessing.cpu_count()
    print("Number of processors available on your system: {}".format(str(process_amount)))
    
    num_processes = [1,2,4] # my system has a maximum of 4 processes 

    list_to_be_sorted = generate_array() # size = 8, max = 20
    start_time = timer()
    sort_process = parallel_merge_sort(list_to_be_sorted,2) # lijst, processes
    end_time = timer()
    duration = end_time - start_time
    print("The parallel merge sort function took {} second(s)".format(duration))