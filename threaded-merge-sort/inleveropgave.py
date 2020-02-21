import threading, logging, time
import concurrent.futures
from random import randint
from typing import List
# import sys
# sys.path.append('/Users/wolfsinem/high-performanced-programming/functions')
# from sort_functions import merge_sort
"""
Mere sort is een efficient sorteeralgoritme. Dit algoritme neemt een array, 
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
    Implementation of the Merge Sort Algortihm: https://www.geeksforgeeks.org/merge-sort/
    Check threaded_merge_sort.png in folder "visuals" for further visual explanation.
    This algorithm will be used for a new function with threads.
    """

    if len(lijst) > 1: 
        num_lijst = len(lijst)
        
        left = lijst[:num_lijst//2]
        right = lijst[num_lijst//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                lijst[k] = left[i] 
                i+=1
            else: 
                lijst[k] = right[j] 
                j+=1
            k+=1
        
        while i < len(left): 
            lijst[k] = left[i] 
            i+=1
            k+=1
        
        while j < len(right): 
            lijst[k] = right[j] 
            j+=1
            k+=1

def threaded_merge_sort(lijst: List[int],threads: int):
    pass


if __name__ == '__main__': 
    lijst = generate_array() 
    print ("Given array is: {}".format(lijst))  
    merge_sort(lijst) 
    print ("Sorted array is: {}".format(lijst))