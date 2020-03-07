/* forkJoin.c
 * ... illustrates the fork-join pattern 
 *      using OpenMP's parallel directive.
 *
 * Huib Aldewereld, HU
 *
 * Compile by: gcc-9 -fopenmp -o forkJoin forkJoin.c
 *
 * Usage: ./forkJoin
 *
 * Exercise:
 * - Compile & run, uncomment the pragma,
 *    recompile & run, compare results.
 */

#include <stdio.h>     // printf()
#include <omp.h>       // OpenMP

int main(int argc, char** argv) {

    int threadsL[] = {1,2,4,8};
    int sizeL = sizeof(threadsL)/sizeof(threadsL[0]);

    printf("size of list with threads %d\n", sizeL);

    for (int i = 0; i < sizeL; i++) {
        omp_set_num_threads(threadsL[i]);
        // printf("amount of threads: %d\n",threadsL[i]);
        // omp_set_num_threads(4);
        #pragma omp parallel
        printf("\nThread number %d...\n",threadsL[i]);
    }
        // #pragma omp parallel num_threads(2)    
        // printf("\nDuring...");
    
        // // omp_set_num_threads(3);
        // #pragma omp parallel
        // printf("\n\nAfter...\n\n");

        return 0;
}


