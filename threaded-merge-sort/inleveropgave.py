import threading, logging, time
import concurrent.futures
from random import randint
from typing import List
# import sys
# sys.path.append('/Users/wolfsinem/high-performanced-programming/functions')
# from sort_functions import merge_sort
def generate_array(size=8,max=20):
    """Create an array of lenght 'size' containing random numbers from the range 0 up to 'max' """
    return [randint(0,max) for _ in range(size)]
    
def merge_sort(xs: List[int]) -> None:
    """In place merge sort of array without recursive. The basic idea
    is to avoid the recursive call while using iterative solution.
    The algorithm first merge chunk of length of 2, then merge chunks
    of length 4, then 8, 16, .... , until 2^k where 2^k is large than
    the length of the array
    """
    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            # merge xs[h:h + 2 * unit]
            
            p, q = l, mid
            while p < mid and q < r:
                # use <= for stable merge merge
                if xs[p] <= xs[q]:
                    p += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2
        
    return xs

# print(generate_array())
# print(merge_sort(generate_array()))