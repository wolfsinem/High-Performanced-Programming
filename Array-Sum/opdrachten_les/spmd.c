/* spmd.c
 * ... illustrates the SPMD pattern in OpenMP,
 * 	using the commandline arguments 
 *      to control the number of threads.
 *
 * Huib Aldewereld, HU, HPP, 2020
 *
 * Compile by: gcc-9 -o spmd -fopenmp spmd.c
 * Usage: ./spmd [numThreads]
 *
 * Exercise:
 * - Compile & run with no commandline args 
 * - Rerun with different commandline args,
 *    note race condition
 * - Uncomment private clause, recompile,
 *    rerun, compare results
 */

#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int id, numThreads;

    printf("\n");
    if (argc > 1) {
        omp_set_num_threads( atoi(argv[1]) );
    }

    #pragma omp parallel private(id)
    {
        id = omp_get_thread_num();
        numThreads = omp_get_num_threads();
        printf("Hello from thread %d of %d\n", id, numThreads);
    }

    printf("\n");
    return 0;
}

// 1 thread
// Hello from thread 0 of 1

// 4 threads 
// Hello from thread 1 of 4
// Hello from thread 1 of 4
// Hello from thread 0 of 4
// Hello from thread 2 of 4

// without args
// = default 4 threads

// uncomment private(id)
// 	- compare results
// 	- can’t notice any difference