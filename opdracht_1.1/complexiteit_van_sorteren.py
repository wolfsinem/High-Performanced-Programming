from numpy import random
from typing import List
import sys
sys.setrecursionlimit(1500)

# python3 -m cProfile complexiteit_van_sorteren.py

def recursive_selection_sort(data: List[int]) -> None:
    # Lists with less than one element are sorted
    if len(data) <= 1:
        return data
    else:
        smallest = min(data)    # find the smallest element in the list
        data.remove(smallest)   # remove from the list
        return [smallest] + recursive_selection_sort(data) # put on front of to be sorted remainder

# recursive_selection_sort(lijst_1)

"""
Genereer random lijsten van lengtes 1'000, 1'000'000 en 1'000'000'000 items. 
Hoe lang heeft elk algoritme nodig om deze te sorteren?
"""
# lijst_1 = list(random.sample(1000)) # 68472 function calls (66300 primitive calls) in 0.251 seconds
# lijst_2 = list(random.sample(1000000))
# lijst_3 = list(random.sample(1000000000)) # error

"""
Genereer een (gesorteerde) lijst van 1'000'000 items. 
Hoe lang heeft elk algoritme nodig om deze te sorteren?
"""
lijst_2_sorted = lijst_2.sort()

"""
Draai de gesorteerde lijst van 1'000'000 items van de vorige vraag achterstevoren (list.reverse()). 
Hoe lang heeft elk algoritme nodig om deze te sorteren?
"""
lijst_2_sorted_reversed = lijst_2_sorted.reverse()

"""
Bekijk / bepaal aan de hand van de algoritmes (en beschrijvingen) hierboven, wat de theoretische run time efficiëntie (Big O) van elk van deze algoritmes is.
Bepaal hiervoor 'best case', 'worst case' en 'average case' run time efficiëntie.
"""

"""
Maakt het voor de complexiteit (Big O) van een algoritme uit of je 
een iteratieve of een recursieve versie beschouwd?
"""