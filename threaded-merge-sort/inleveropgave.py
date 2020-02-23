from random import randint
import multiprocessing
import math
from timeit import default_timer as timer
from typing import List
import matplotlib.pyplot as plt

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

    left = merge_sort(lijst[:int(len(lijst)/2)])
    right = merge_sort(lijst[int(len(lijst)/2):])

    return merge(left,right)


def merge(*args):
    """Merge the sublists"""
    
    new_lijst = []
    
    left, right = args[0] if len(args) == 1 else args

    l=0
    r=0
    
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            new_lijst.append(left[l])
            l += 1
        else:
            new_lijst.append(right[r])
            r += 1
    if l == len(left):
        new_lijst.extend(right[r:])
    else:
        new_lijst.extend(left[l:])
    
    return new_lijst


def split_for_threading(lijst: List[int], processes: int):
    """
    Param_ lijst: generated list with x integers
    Param processes: number of processes being used
    Var split: divides the list by the amount of processes 
    """
    split = int(math.ceil(float(len(lijst)) / processes))
    split_list = [lijst[i * split:(i + 1) * split] for i in range(processes)]
    
    full_list = []
    for i in split_list:
        if i != []:
            full_list.append(i)
            
    return full_list


def parallel_merge_sort(lijst: List[int], processes: int):
    """
    The pool object offers parallelization of the merge sort
    function. 
    https://docs.python.org/2/library/multiprocessing.html
    """
    pool = multiprocessing.Pool(processes=processes)

    splitted_list = split_for_threading(lijst,processes)
    lijst = pool.map(merge_sort, splitted_list)

    while len(lijst) > 1:
        extra = lijst.pop() if len(lijst) % 2 == 1 else None
        lijst = [(lijst[i], lijst[i + 1]) for i in range(0, len(lijst), 2)]
        lijst = lijst = pool.map(merge,lijst) + ([extra] if extra else [])

        return lijst[0]


def set_time(lijst: List[int], processes: int):
    """
    Function that measures the execution time for
    each choosen amount of processors
    """
    results = []

    for i in processes:
        start_time = timer()
        sort_process = parallel_merge_sort(lijst,i)
        end_time = timer()
        duration = end_time - start_time
        
        results.append(duration)
        print('Parallel Merge Sort with {} process(es) took {:.4f} second(s)'.format(i,duration))
    return results

def plot_me(processes: List[int], result: List[int]):
    """
    Plot all the results of the time execution
    using the matplotlib library
    """
    plt.scatter(processes, result, label=f"Processes: {processes}; Duration: {result}")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.savefig('parallel_programming_merge_sort.png')
    plt.show()


if __name__ == "__main__":
    # process_amount = multiprocessing.cpu_count()
    # print("Number of processors available on your system: {}".format(str(process_amount)))

    processes = [1,2,4]
    list_to_be_sorted = generate_array() # default size = 8, max = 20
    set_time(list_to_be_sorted,processes)           # lijst, processes 
    
    resultaten = set_time(list_to_be_sorted,processes)
    plot_me(processes,resultaten)