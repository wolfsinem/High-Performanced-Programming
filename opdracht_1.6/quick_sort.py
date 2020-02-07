import sys
sys.path.append('/Users/wolfsinem/High-Performanced-Programming/opdracht_1.5')
from bucket_sort import generate_random_list
import numpy as np
import timeit

def partitioning_step(lijst):
    lijst_low = []
    lijst_equal = [] 
    lijst_high = [] 

    if len(lijst) <2:
        return lijst
    
    pivot = lijst[0]
    
    for i in range(len(lijst)):
        if lijst[i] < pivot:
            lijst_low.append(lijst[i])
        elif lijst[i] == pivot:
            lijst_equal.append(lijst[i])
        else:
            lijst_high.append(lijst[i])

    sorted_list = partitioning_step(lijst_low) + [pivot] + partitioning_step(lijst_high)
    return sorted_list
# print(partitioning_step(generate_random_list(10)))

def timer(function):
    start_time = timeit.default_timer()
    function
    print('This algorithm took {:.10f} seconds'.format((timeit.default_timer() - start_time)))
timer(partitioning_step(generate_random_list(600000)))


"""
----------------------------
Tijd complexiteit Quick Sort 
----------------------------

Best case en Average case = O(n log(n))
    In de meest gebalanceerde scenario split je de lijsten in twee gelijke delen waarin beide delen
    dus evenveel gegenereerde getallen heeft. 

Worst case = (n^2)
    Dit komt voor wanneer de pivot die wordt gekozen uit de lijst, het grootste getal is 
    of juist het kleinste getal. Daarnaast wanneer alle gegenereerde getallen in de lijst hetzelfde
    blijken te zijn. 


Voor een lijst met 10 random gegenereerde getallen duurde het ongeveer 0.0000009537 seconden

30.000 = 0.0000021458
600.0000= 0.0000011921

Opvallend aan het quick sort algoritme is het feit dat een lijst met meer gegenereerde getallen,
sneller opgelost wordt dan een lijst met veel minder getallen. 
"""