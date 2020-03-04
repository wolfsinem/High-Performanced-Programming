/* parallelForStripes.c
 * ... illustrates how to make OpenMP map threads to 
 *	parallel for-loop iterations in 'stripes' instead of blocks
 *	(use only when not accesssing memory).
 *
 * Huib Aldewereld, HU, HPP, 2020
 *
 * Compile by: gcc-9 -o parallelForStripes -fopenmp parallelForStripes.c
 * Usage: ./parallelForStripes [numThreads]
 * 
 * Exercise:
 * - Compile, run, compare output to 'Blocks' version
 */

#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    const int REPS = 8;

    printf("\n");
    if (argc > 1) {
        omp_set_num_threads( atoi(argv[1]) );
    }

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int numThreads = omp_get_num_threads();
        int i;
        for (i = id; i < REPS; i += numThreads) {
            printf("Thread %d performed iteration %d\n", 
                     id, i);
        }
    }

    printf("\n");
    return 0;
}

// blocks output with 3 threads
// Thread 1 performed iteration 3
// Thread 1 performed iteration 4
// Thread 2 performed iteration 6
// Thread 2 performed iteration 7
// Thread 0 performed iteration 0
// Thread 0 performed iteration 1
// Thread 0 performed iteration 2
// Thread 1 performed iteration 5

// stripes output with 3 outputs
// Thread 1 performed iteration 1
// Thread 1 performed iteration 4
// Thread 2 performed iteration 2
// Thread 2 performed iteration 5
// Thread 0 performed iteration 0
// Thread 0 performed iteration 3
// Thread 1 performed iteration 7
// Thread 0 performed iteration 6
