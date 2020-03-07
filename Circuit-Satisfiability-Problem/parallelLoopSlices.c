/* parallelForSlices.c
 * ... illustrates the parallel for loop pattern in MPI 
 *	in which processes perform the loop's iterations in 'slices' 
 *	(simple, and useful when loop iterations do not access
 *	 memory/cache locations) ...
 * Huib Aldewereld, HU, HPP, 2020
 * 
 * 
 * compile: mpicc -o main parallelLoopSlices.c
 * run: ./main
 */

#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
	const int REPS = 4;
	int id = -1, numProcesses = -1, i = -1;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &id);
	MPI_Comm_size(MPI_COMM_WORLD, &numProcesses);

	for (i = id; i < REPS; i += numProcesses) {
		printf("Process %d is performing iteration %d\n",
			id, i);
	}

	MPI_Finalize();
	return 0;
}


// output with 8 threads:
// Process 0 is performing iteration 0
// Process 0 is performing iteration 1
// Process 0 is performing iteration 2
// Process 0 is performing iteration 3
// Process 0 is performing iteration 4
// Process 0 is performing iteration 5
// Process 0 is performing iteration 6
// Process 0 is performing iteration 7

// output with 4 threads:
// Process 0 is performing iteration 0
// Process 0 is performing iteration 1
// Process 0 is performing iteration 2
// Process 0 is performing iteration 3