# Computes an approximation of Pi by summing up
# a series of terms.  The more terms, the closer
# the approximation.
# Based on a variation of the Gregory-Leibniz series approximation

"""
In veel gevallen wil je niet alleen threads forken, maar wil je aan het 
einde ook de resultaten van de berekeningen in elke thread weer samenvoegen.
"""

import threading

def f( x ):
    """
    The function being integrated, and which returns
    an approximation of Pi when summed up over an interval
    of integers.
    """
    return 4.0 / ( 1 + x*x )

class WorkerThread(threading.Thread):
    
    def __init__(self, args):
        """
        args must contain n1, n2, and deltaX, in that order.
        """
        threading.Thread.__init__(self, args=args)
        self.n1 = args[0]
        self.n2 = args[1]
        self.deltaX = args[2]
    
    def run(self):
        """
        This will be called automatically by start() in
        main.  It's the method that does all the work.
        """
        pass # TODO: Replace with actual code!
    
    def get(self):
        """
        gets the computed sum.
        """
        pass # TODO: Replace with actual code!

def main():
    """
    Gets a number of terms from the user, then sums
    up the series and prints the resulting sum, which
    should approximate Pi.
    """

    # get the number of terms
    N = int( input( "> " ) )

    sum = 0.0          # where we sum up the individual
                       # intervals
    deltaX = 1.0 / N   # the interval

    # sum over N terms
    for i in range( N ):
        sum += f( i * deltaX )

    # display results
    print( "sum = %1.9f" % ( sum * deltaX ) )

main()