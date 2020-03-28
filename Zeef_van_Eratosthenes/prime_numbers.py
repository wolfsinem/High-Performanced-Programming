# coding=utf-8
"""
--THEORIE--
Zeef van Eratosthenes

Dit is een algoritme uit 240 v.Chr. om priemgetallen te vinden. 
Deze elegante methode is vooral efficiënt wanneer hij wordt 
gebruikt voor de kleinere priemgetallen.

    1) Maak een gesorteerde lijst van alle getallen van 2 tot een maximum. 
    2) Kies het kleinste getal uit de lijst.
    3) Streep alle veelvouden van het gekozen getal door.
    4) Kies het volgende getal uit de lijst en ga verder met stap 3.

note: een priemgetal is een getal groter dan 1 dat slechts deelbaar is door zichzelf en het getal 1
"""
import time

start_time = time.time()

def priemgetal(maximum):
    priem = [] # array met alle priemgetallen vanaf 2 t/m een maximum
    count = 0 # totaal aantal priemgetallen
    k = 2 

    for i in range(k, maximum):
        priem.append(i)

    # Loop door de lijst 
    for j in priem:
        count += 1
        for i in priem:
            if i % j == 0:
                if i != j:
                    priem.remove(i)
    return priem, count

priemgetallen, count = priemgetal(100)
total_time = time.time() - start_time

print("Totaal: {}".format(count))
print("Lijst van alle priemgetallen: {}".format(priemgetallen))
print("Sequential algorithm took: {:.5f} second(s)".format(total_time))

# Verifieer de eeste n priemgetallen: https://miniwebtool.com/first-n-prime-numbers/?number=10 
echte_priemgetallen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
pg_2 = priemgetal(30)[0]
if echte_priemgetallen == pg_2:
    print("De priemgetallen zijn geverifieerd")
else: 
    print("De priemgetallen zijn niet identiek, wijzig het programma")