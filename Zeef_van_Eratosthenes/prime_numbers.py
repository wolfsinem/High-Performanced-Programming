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


--OPDRACHT--
1) Creeër de zeef -- een dynamische array van 2 tot N (dit kan een array van booleans zijn, 
   of ints of wat dan ook waar je random access toe kan hebben en eenvoudig gebruikt kan 
   worden om bepaalde elementen te "markeren").

2) Aangezien 1 geen priem is, zetten we k op 2.

3) Loop totdat k2 > N:
    3.1) In de zeef, markeer alle elementen op de indexen die een veelvoud zijn van k tussen 
         k2 en N (inclusief).
    3.2) Vind de kleinste index groter dan k die niet gemarkeerd is, en zet k op deze waarde.

4) De indexen van de niet gemarkeerde elementen in de zeef zijn priemgetallen.
"""
import time

start_time = time.time()

# sequentiele variant van het algoritme
def priemgetal(maximum):
    # Array met getallen vanaf 2 t/m een maximum
    priem = []
    # maximum = int(input("Voer een getal voor het maximum in: "))
    for i in range(2, maximum):
        priem.append(i)
    # print(priem)

    # Loop door de lijst 
    for j in priem:
        for i in priem:
            if i % j == 0:
                if i != j:
                    priem.remove(i)

    # print(priem)
    return priem

priemgetallen = priemgetal(100)
total_time = time.time() - start_time

print("Sequential algorithm took: {:.5f} second(s)".format(total_time))
print("List of prime numbers: {}".format(priemgetallen))