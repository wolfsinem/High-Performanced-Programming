/* parallelForBlocks.c
 * ... illustrates the use of OpenMP's default parallel for loop
 *  	in which threads iterate through blocks of the index range
 *	(cache-beneficial when accessing adjacent memory locations).
 *
 * Huib Aldewereld, HU, HPP, 2020
 *
 * Compile by: gcc -o parallelForBlocks -fopenmp parallelForBlocks.c
 * Usage: ./parallelForBlocks [numThreads]
 *
 * Exercise
 * - Compile, run, trace execution
 */

#include <stdio.h>    // printf()
#include <stdlib.h>   // atoi()
#include <omp.h>      // OpenMP

int main(int argc, char** argv) {
    const int REPS = 8;
    int id, i;

    printf("\n");
    if (argc > 1) {
        omp_set_num_threads( atoi(argv[1]) );
    }

    #pragma omp parallel for private(id, i) 
    for (i = 0; i < REPS; i++) {
        id = omp_get_thread_num();
        printf("Thread %d performed iteration %d\n", 
                 id, i);
    }

    printf("\n");
    return 0;
}


