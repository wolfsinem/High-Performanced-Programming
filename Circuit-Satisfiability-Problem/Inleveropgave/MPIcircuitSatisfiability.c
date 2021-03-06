/* circuitSatifiability.c solves the Circuit Satisfiability
 *  Problem using a brute-force sequential solution.
 *
 *   The particular circuit being tested is "wired" into the
 *   logic of function 'checkCircuit'. All combinations of
 *   inputs that satisfy the circuit are printed.
 *
 *   16-bit version by Michael J. Quinn, Sept 2002.
 *   Extended to 32 bits by Joel C. Adams, Sept 2013.
 *   Adapted for HU-HPP by Huib Aldewereld, 2020.
 * 
 *   compile: mpicc MPIcircuitSatisfiability.c -Wall -ansi -pedantic -std=c99 -o main
 *   run: mpirun -np 1 ./main
 */

#include <stdio.h>                                             // printf()
#include <limits.h>                                            // UINT_MAX
#include <mpi.h>                                               // include MPI header file

int checkCircuit (int, long);

int main (int argc, char *argv[]) {
   long i;                                                     // loop variable (64 bits) 
   int id = 0;                                                 // process id 
   int local_sum = 0;                                          // number of solutions 

   unsigned int max_pr = UINT_MAX;                             // maximum value for an object of type unsigned int 
   int numProcesses = 0;                                       // amount of processes being used
   
   double startTime = 0.0, totalTime = 0.0;                    // start and total of elapsed time
   startTime = MPI_Wtime();

   /* Using parallelLoopSlices.c as an example in this part
    *
    * MPI_init       =  Initialize the MPI environment
    * MPI_Comm_rank  =  Get the rank of the process
    * MPI_Comm_size  =  Get the number of processes
    */
   
   MPI_Init(&argc, &argv);
   MPI_Comm_rank(MPI_COMM_WORLD, &id);
   MPI_Comm_size(MPI_COMM_WORLD, &numProcesses);
   
   printf("\nProcess %d is checking the circuit...\n", id);

   for (i = id; i < max_pr; i+= numProcesses) {                           
      local_sum += checkCircuit (id, i);
   }

   totalTime = MPI_Wtime() - startTime;
   printf("Process %d finished in time %f seconds with a total of: %d solutions\n", id, totalTime, local_sum);

   /* MPI_Reduce takes an array of input elements on each process and 
    * returns an array of output elements to the root process.
    * https://mpitutorial.com/tutorials/mpi-reduce-and-allreduce/
    */ 

   int global_sum = 0; // number of solutions 
   MPI_Reduce(&local_sum, &global_sum, 1, MPI_INT, MPI_SUM, 0,MPI_COMM_WORLD); 
   
   // clean up
   MPI_Barrier(MPI_COMM_WORLD);
   MPI_Finalize();

   totalTime = MPI_Wtime() - startTime;
   if (id == 0) {
         printf("Total sum = %d\n", global_sum);
         printf("Total time = %f\n", totalTime); 
}
   // fflush (stdout);
   

   return 0;
}

/* EXTRACT_BIT is a macro that extracts the ith bit of number n.
 *
 * parameters: n, a number;
 *             i, the position of the bit we want to know.
 *
 * return: 1 if 'i'th bit of 'n' is 1; 0 otherwise 
 */

#define EXTRACT_BIT(n,i) ( (n & (1<<i) ) ? 1 : 0)

/* checkCircuit() checks the circuit for a given input.
 * parameters: id, the id of the process checking;
 *             bits, the (long) rep. of the input being checked.
 *
 * output: the binary rep. of bits if the circuit outputs 1
 * return: 1 if the circuit outputs 1; 0 otherwise.
 */

#define SIZE 32

int checkCircuit (int id, long bits) {
   int v[SIZE];        /* Each element is one of the 32 bits */
   int i;

   for (i = 0; i < SIZE; i++) {
     v[i] = EXTRACT_BIT(bits,i);
   }

   if ( ( (v[0] || v[1]) && (!v[1] || !v[3]) && (v[2] || v[3])
       && (!v[3] || !v[4]) && (v[4] || !v[5])
       && (v[5] || !v[6]) && (v[5] || v[6])
       && (v[6] || !v[15]) && (v[7] || !v[8])
       && (!v[7] || !v[13]) && (v[8] || v[9])
       && (v[8] || !v[9]) && (!v[9] || !v[10])
       && (v[9] || v[11]) && (v[10] || v[11])
       && (v[12] || v[13]) && (v[13] || !v[14])
       && (v[14] || v[15]) )
       &&
          ( (v[16] || v[17]) && (!v[17] || !v[19]) && (v[18] || v[19])
       && (!v[19] || !v[20]) && (v[20] || !v[21])
       && (v[21] || !v[22]) && (v[21] || v[22])
       && (v[22] || !v[31]) && (v[23] || !v[24])
       && (!v[23] || !v[29]) && (v[24] || v[25])
       && (v[24] || !v[25]) && (!v[25] || !v[26])
       && (v[25] || v[27]) && (v[26] || v[27])
       && (v[28] || v[29]) && (v[29] || !v[30])
       && (v[30] || v[31]) ) )
   {
      printf ("%d) %d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d \n", id,
         v[31],v[30],v[29],v[28],v[27],v[26],v[25],v[24],v[23],v[22],
         v[21],v[20],v[19],v[18],v[17],v[16],v[15],v[14],v[13],v[12],
         v[11],v[10],v[9],v[8],v[7],v[6],v[5],v[4],v[3],v[2],v[1],v[0]);
      fflush (stdout);
      return 1;
   } else {
      return 0;
   }
}

