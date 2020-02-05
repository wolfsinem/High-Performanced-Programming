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

Bron: https://www.growingwiththeweb.com/2015/06/bucket-sort.html
"""

lijst = [random.randint(1,100) for x in range(10)] # array van 10 elementen

def bucket_sort(lijst,num_steps):
    """get the right digit of an integer and store it in a new array"""
    print(lijst)
    last_element = []
    for i in lijst:
        last_element.append(i % (10 ** 1))
    print(last_element)
    max_value = max(last_element)
    min_value = min(last_element)
    # print(max_value)

    """make 10 buckets in a dictionary in which the integers will be sorted, from 0 to 9"""
    buckets = {i:[] for i in range(0,int(num_steps))}
    print(buckets)

    # for i in last_element:
    #     for j in buckets:
    #         if i == j:
    #             buckets.append(i)
    # value = next( v for i, v in enumerate(lijst.itervalues()) if i == index )
    
    
    """print key and values of dict"""
    # for k, v in buckets.items():
    #    print "%s: %s" % (k, v)

bucket_sort(lijst,10)

# arr[]
# N = aantal elementen in de array
# max = maximale waarde
# min = minimale waarde

# b = er zijn tien verschillende 'buckets', van 0 t/m 9. 

# formule:
# ceil ( ( max ( lijst ) + 1 ) / bucket )

# b[j] = arr[i]
# j = floor(arr[i]/divider)
