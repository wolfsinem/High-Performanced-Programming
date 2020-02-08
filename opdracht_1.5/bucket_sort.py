from numpy import random
import math

"""
Plaats elke waarde van de een-dimensionale array in een rij van de bucket array,
gebaseerd op het meest rechtse cijfer in het getal (de "een"-waarde). 
Bijvoorbeeld, 97 wordt geplaatst in rij 7, 3 wordt geplaatst in rij 3 en 100 wordt geplaatst in rij 0. 
Deze stap heet de distribution pass.
        
        functie die dit doet: 
                            (element % 10 ** digits)

Loop door de bucket array rij voor rij, en kopieer de waardes terug in de originele array. 
Deze stap heet de gathering pass. De volgorde van de hierboven genoemde getallen is dus nu 100, 3, 97.

Herhaal dit proces voor elke volgende digit-positie (dus voor de tientallen, honderdtallen, etc.). 
Na de laatste gathering pass is de array gesorteerd.

array index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
element     | n | . | . | . | . | . | . | . | . | . |

ceil ( ( max ( lijst ) + 1 ) / bucket )

Bron: https://www.growingwiththeweb.com/2015/06/bucket-sort.html
"""

def generate_random_list(num_steps):
    lijst = [random.randint(1,100) for x in range(num_steps)]
    return lijst

lijst = generate_random_list(10)

def bucket_sort(lijst,num_steps):
    """get the right-sided digit of an integer and store it in a new array"""
    last_elements = []
    for i in lijst:
        last_elements.append(i % (10 ** 1))
    # print(lijst)
    print(last_elements)

    # max_value = max(lijst)
    # min_value = min(lijst)
    # print(max_value)

    """make 10 buckets in which the integers will be sorted, from 0 to 9"""
    buckets = []
    i = 0
    while(i<num_steps):
        buckets.append([])
        i+=1
    print(buckets)

    max_value = max(last_elements)
    
    # for i in last_elements:
    #     if 
        


    # for i in last_elements:

# print(bucket_sort(lijst,10))


        # print(str(i) + " goes in " + str())

# Bepaal, net als eerder, op basis van een test en door analyse, de Big O waarde van Bucket Sort.

# Best case: 
#     O(n+k), als de getallen in de lijst zo zijn gegenereerd dat er per bucket maar 1 getal voorkomt waardoor
#     het eigenlijk al is gesorteerd en je per bucket niet meer hoeft te sorteren. 

# Average case: 
#     O(n+k), 

# Worst case: 
#     O(n^2), de worst case is wanneer de meeste getallen in de lijst bij elkaar in de zelfde bucket komen.
#     Stel je hebt de getallen 12,22,32,42,52,62, dan komen ze allemaal in dezelfde bucket (2) en duurt het langer om te sorteren.