import sys
sys.path.append('/Users/wolfsinem/High-Performanced-Programming/opdracht_1.5')
from bucket_sort import generate_random_list
import numpy as np
import timeit

def quick_sort(lijst):
    # if there is only 1 element or 0, you need to stop the recursion
    if len(lijst) < 2:
        return lijst
    
    # select any index in the list to be the pivot such that all the elements less than the pivot 
    # go to the left and the elements greater than the pivot go the the right.
    pivot = lijst[0]
    
    list_low = []
    list_high = [] 

    """partitioning step"""
    for number in lijst[1:]:
        if number < pivot:
            list_low.append(number)
        else: 
            list_high.append(number)
            
    return quick_sort(list_low) + [pivot] + quick_sort(list_high)
# print(quick_sort(generate_random_list(10)))

def timer(function):
    start_time = timeit.default_timer()
    function
    print('This algorithm took {:.10f} seconds'.format((timeit.default_timer() - start_time)))
# timer(quick_sort(generate_random_list(100)))


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