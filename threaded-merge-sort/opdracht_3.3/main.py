# coding=utf-8
import threading, logging, time
import concurrent.futures

"""
Canvas opdracht 3.3 Race Conditions

Voor we verder gaan met de geavanceerdere onderdelen van de threading module 
voor synchronizatie, hebben we eerst een voorbeeld nodig om aan te tonen wat een 
Race Condition is. || Race Conditions || zijn problemen die optreden als meerdere
processen/threads tegelijkertijd variabelen proberen te (over)schrijven.

Race conditions kunnen optreden als je twee of meer threads draait die een stuk 
data delen. In dit voorbeeld gaan we proberen om een duidelijke race condition te 
creëren, die elke keer optreedt. In veel gevallen treden race conditions maar af-en-toe op,
waardoor ze ook zo lastig zijn om te debuggen (het programma doet soms "ineens" niet meer 
wat er verwacht wordt).

In dit voorbeeld maken we een class die een simpele database moet voorstellen. 
Deze FakeDatabase heeft __init__( ) en update( ) methodes:
"""

class FakeDatabase:
    def __init__(self):
        self.value = 0


    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)


"""
21:01:09: Testing update. Starting value is 0.
21:01:09: Thread 0: starting update
21:01:09: Thread 1: starting update
21:01:09: Thread 0: finishing update
21:01:09: Thread 1: finishing update
21:01:09: Testing update. Ending value is 1.
"""