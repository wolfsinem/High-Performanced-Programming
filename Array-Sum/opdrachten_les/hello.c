#include <omp.h>
#include <stdio.h>
#include <stdlib.h>


int main (int argc, char** argv)
{
  int numThreads;
  int var = 5;

  if (argc > 1) {
        omp_set_num_threads( atoi(argv[1]) );
}

#pragma omp parallel //print meer dan 1x
{
  numThreads = omp_get_thread_num();
  var = var + omp_get_thread_num();
  printf("Hello World from thread: %d var is %d\n", numThreads,var);
}

  return 0;

}

/* ouput:
 * Hello World from thread: 0 var is 5
 * Hello World from thread: 1 var is 6
 */