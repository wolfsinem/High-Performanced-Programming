# coding=utf-8
import logging
import threading
import time

"""
Canvas opdracht 3.1 Threads in Python

In Python kan je gebruik maken van de threading module 
om parallelle threads te definiëren en te draaien.
"""

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2) # wait for 2 seconds
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")


"""
start = time.perf_counter >> tijd begint hier

def hier_een_functie()
    print('sleep 1 sec')
    time.sleep(1)
    print('done sleep')

hier_een_functie() --> run hier de functie 

end = time.perf_counter >> tijd eindigt hier

duur = end-start
"""