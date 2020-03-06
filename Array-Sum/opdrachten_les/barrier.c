/* barrier.c
 * ... illustrates the use of the OpenMP barrier command,
 * 	using the commandline to control the number of threads...
 *
 * Huib Aldewereld, HU, HPP, 2020
 *
 * Compile by: gcc-9 -o barrier -fopenmp barrier.c
 * Usage: ./barrier [numThreads]
 * 
 * Exercise:
 * - Compile & run several times, noting interleaving of outputs.
 * - Uncomment the barrier directive, recompile, rerun,
 *   and note the change in the outputs.
 */

#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    printf("\n");
    if (argc > 1) {
        omp_set_num_threads( atoi(argv[1]) );
    }

    #pragma omp parallel 
    {
        int id = omp_get_thread_num();
        int numThreads = omp_get_num_threads();
        printf("Thread %d of %d is BEFORE the barrier.\n", id, numThreads);

       #pragma omp barrier 

        printf("Thread %d of %d is AFTER the barrier.\n", id, numThreads);
    }

    printf("\n");
    return 0;
}

// 1 thread
// Thread 0 of 1 is BEFORE the barrier.
// Thread 0 of 1 is AFTER the barrier.

// 2 threads
// Thread 1 of 2 is BEFORE the barrier.
// Thread 1 of 2 is AFTER the barrier.
// Thread 0 of 2 is BEFORE the barrier.
// Thread 0 of 2 is AFTER the barrier.

// <<< with pragma omp parallel >>>

// 2 threads
// Thread 0 of 2 is BEFORE the barrier.
// Thread 1 of 2 is BEFORE the barrier.
// Thread 0 of 2 is AFTER the barrier.
// Thread 1 of 2 is AFTER the barrier.

// note: when using pragma omp parallel every thread will print the "BEFORE" statement first
    //   and the "AFTER" statement just how it should be. BEFORE comes before.. 
