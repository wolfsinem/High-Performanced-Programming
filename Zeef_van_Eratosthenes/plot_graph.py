import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

"""Data generated by running the Sieve of Eratosthenes sequentialy and parallel in parallel_sieve.py"""

data = {'Processes': ['sequential',1,2,4,8],
        '10': [0.00001,
               0.0015,
               0.00031,
               0.00142,
               0.00854], 
        '100': [0.00007,
               0.00017,
               0.00040,
               0.00516,
               0.02015], 
        '1000':[0.00547,
               0.01,
               0.00535,
               0.00575,
               0.02063], 
        '10000':[0.25710,
               0.54,
               0.36088,
               0.37576,
               0.39939],
        '100000': [23.49,
               42.62,
               23.29,
               29.09,
               27.82] }

def plot(data):
    """Plot generated data"""
    df = pd.DataFrame(data)
    ax = df.plot(x='Processes',title='speed-up efficieny, but not really')
    ax.set(xlabel="Amount of processes", ylabel="Elapsed time in second(s)")
    # plt.savefig('so called speed-up efficiency.png')
    plt.show()

plot(data)