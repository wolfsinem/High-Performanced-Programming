/*  omp_arraySum.c uses OpenMP to sum the values in an input file,
 *  whose name is specified on the command-line.
 *  
 *  Based on arraySum.c - Huib Aldewereld
 *  
 *  compile gcc-9 -fopenmp -o main omp_arraySum.c 
 *  run ./main
 */

#include <stdio.h>      /* I/O stuff */
#include <stdlib.h>     /* calloc, etc. */
#include <omp.h>        /* OpenMP */

void readArray(char * fileName, 
               double ** a, 
               int * n);

double parallelSumArray(double * a,
                int numValues);

int main(int argc, char * argv[])
{
  int  howMany;
  double sum;
  double * a;
  double start; // start elapsed wall clock time in seconds 
  double end; // end elapsed wall clock time in seconds

  // int nThreads = omp_get_max_threads(); // returns an upper bound on the number of threads
  int threads[] = {1,2,4,8};
  int sizeT = sizeof(threads)/sizeof(threads[0]);
  printf("Size of list with threads: %d\n", sizeT);

  if (argc != 2) {
    fprintf(stderr, "\n*** Usage: arraySum <inputFile>\n\n");
    exit(1);
  }
  
  readArray(argv[1], &a, &howMany);
  
  for (int i = 0; i < sizeT; i++) {
      omp_set_num_threads(threads[i]);

      #pragma omp parallel

      start = omp_get_wtime(); 
      sum = parallelSumArray(a, howMany);
      end = omp_get_wtime();

      printf("Elasped time = %f seconds using %d thread(s)\n", end - start,threads[i]);
  // printf("The sum of the values in the input file '%s' is %g\n",argv[1], sum);
  
  } 

  free(a);

  return 0;
  
}

/* readArray fills an array with values from a file.
 * Receive: fileName, a char*,
 *          a, the address of a pointer to an array,
 *          n, the address of an int.
 * PRE: fileName contains N, followed by N double values.
 * POST: a points to a dynamically allocated array
 *        containing the N values from fileName
 *        and n == N.
 */

void readArray(char * fileName, double ** a, int * n) {
  int count, howMany;
  double * tempA;
  FILE * fin;

  fin = fopen(fileName, "r");
  if (fin == NULL) {
    fprintf(stderr, "\n*** Unable to open input file '%s'\n\n",
                     fileName);
    exit(1);
  }

  fscanf(fin, "%d", &howMany);
  tempA = calloc(howMany, sizeof(double));
  if (tempA == NULL) {
    fprintf(stderr, "\n*** Unable to allocate %d-length array",
                     howMany);
    exit(1);
  }

  for (count = 0; count < howMany; count++)
   fscanf(fin, "%lf", &tempA[count]);

  fclose(fin);

  *n = howMany;
  *a = tempA;
}

/* parallelSumArray sums the values in an array of doubles.
 * Receive: a, a pointer to the head of an array;
 *          numValues, the number of values in the array.
 * Return: the sum of the values in the array.
 */

double parallelSumArray(double * a, int numValues) {
  int i;
  double result = 0.0;

  #pragma omp parallel for reduction(+:result) // reduction.c 
  for (i = 0; i < numValues; i++) {
    result += a[i];
  }

  return result;
}