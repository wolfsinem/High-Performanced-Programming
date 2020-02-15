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

num_steps = len(lijst)
max_value = max(lijst)

buckets_list = []
i = 0
while(i<num_steps):
    buckets_list.append([])
    i+=1

"""distribution pass"""
for i in lijst:
    # for this algorithm we will sort the integers in the first round depending on its right index
    right_index = i % (10 ** 1)
    buckets_list[right_index].append(i)

print(buckets_list)

"""gathering pass"""
lijst = []
for i in buckets_list:
    for j in i:
        lijst.append(j)
print(lijst)

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


# def bucket_sort(lijst,num_steps):
#     """make 10 buckets in which the integers will be sorted, from 0 to 9"""
#     buckets_list = []
#     i = 0
#     while(i<num_steps):
#         buckets_list.append([])
#         i+=1

#     max_value = max(lijst)
    
#     """sort each item in list to bucket"""
#     for i in lijst:
#         num = (int(math.ceil((i/max_value)*len(buckets_list))))
#         buckets_list[num-1].append(i)
    
#     out_bucket = [num for bucket in buckets_list for num in sorted(bucket)]
    
#     return out_bucket

#         lijst = [j for bucket in generated_buckets for j in bucket]


# lijst = [42,5,124,2]
# for i in lijst:
#     index = i // 10**(len(str(i))-1) % 10
#     print(index)


    """Distribution pass"""
#     for i in lijst:
#         # for this algorithm we will sort the integers in the first round depending on its right index
#         index = i % (10 ** 1)
#         buckets_list[index].append(i)
#     print("List with filled buckets: {}".format(buckets_list))