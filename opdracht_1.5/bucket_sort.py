from numpy import random

# Plaats elke waarde van de een-dimensionale array in een rij van de bucket array,
# gebaseerd op het meest rechtse cijfer in het getal (de "een"-waarde). 
# Bijvoorbeeld, 97 wordt geplaatst in rij 7, 3 wordt geplaatst in rij 3 en 100 wordt geplaatst in rij 0. 
# Deze stap heet de distribution pass.

# Loop door de bucket array rij voor rij, en kopieer de waardes terug in de originele array. 
# Deze stap heet de gathering pass. De volgorde van de hierboven genoemde getallen is dus nu 100, 3, 97.

# Herhaal dit proces voor elke volgende digit-positie (dus voor de tientallen, honderdtallen, etc.). 
# Na de laatste gathering pass is de array gesorteerd.
lijst = [random.randint(1,100) for x in range(10)] # array van 10 elementen

def bucket_sort(lijst):
    pass

# array index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
# element     | n | . | . | . | . | . | . | . | . | . |
