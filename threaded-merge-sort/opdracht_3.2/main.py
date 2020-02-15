# coding=utf-8
import logging
import threading
import time

"""
Canvas opdracht 3.2 Multiple Threads

In de vorige opgave hebben we laten zien hoe je met twee threads 
(1 fork en de hoofd-thread) kan werken, maar in veel gevallen wil 
je met meerdere threads aan de gang. Hiervoor zijn een lastige 
manier en een eenvoudigere manier.

De lastigere manier is om het met de hand zelf te regelen. 
Pas de code van je forkJoin-voorbeeld aan (vervang vanaf 
regel 15 (29) met de volgende code):
"""

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2) # wait for 2 seconds
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,)) 
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)



"""
start = time.perf_counter >> tijd begint hier

def hier_een_functie(seconds)
    print('sleep {} sec'.format(seconds))
    time.sleep(seconds)
    print('done sleep')
-----------------------------------------------------------------------
- i.p.v. functies twee keer uit laten voeren kun je threading gebruiken

hier_een_functie() --> run hier de functie 
hier_een_functie() --> run hier de functie 
-----------------------------------------------------------------------
- import threading

t1 = threading.Thread(target=hier_een_functie) --> dont execute the function so no parentheses
t2 = threading.Thread(target=hier_een_functie)

t1.start()
t2.start()

t1.join()
t1.join()
-----------------------------------------------------------------------
- create a while loop instead of whats written above

threads = [] --> create a list with threads to loop over with join 

for _ in range(10): --> use _ as a throw-away variable because you only want to loop over 
    t = threading.Thread(target=hier_een_functie, args=[1.5]) --> hier_een_functie() takes seconds as args 
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
-----------------------------------------------------------------------
end = time.perf_counter >> tijd eindigt hier

duur = end-start

if you loop in a range of 10 for 1.5 seconds, it would normally take 15 seconds to finish
but with threads its finished in 1.51 seconds
"""

## code will look like this with threading
# start = time.perf_counter

# def hier_een_functie(seconds)
#     print('sleep {} sec'.format(seconds))
#     time.sleep(seconds)
#     print('done sleep')

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=hier_een_functie, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# end = time.perf_counter
# print('finished in {} seconds'.format(end-start))

####################################################################

# import concurrent.futures
# start = time.perf_counter

# def hier_een_functie(seconds)
#     print('sleep {} sec'.format(seconds))
#     time.sleep(seconds)
#     return 'done sleeping..{seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]   
#     results = [executor.submit(hier_een_functie, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#           print(f.result())


# end = time.perf_counter
# print('finished in {} seconds'.format(end-start))