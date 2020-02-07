import sys
sys.path.append('/Users/wolfsinem/High-Performanced-Programming/opdracht_1.5')
from bucket_sort import generate_random_list
import numpy as np

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

print(partitioning_step(generate_random_list(10)))