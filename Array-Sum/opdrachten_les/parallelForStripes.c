/* parallelForStripes.c
 * ... illustrates how to make OpenMP map threads to 
 *	parallel for-loop iterations in 'stripes' instead of blocks
 *	(use only when not accesssing memory).
 *
 * Huib Aldewereld, HU, HPP, 2020
 *
 * Compile by: gcc -o parallelForStripes -fopenmp parallelForStripes.c
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


