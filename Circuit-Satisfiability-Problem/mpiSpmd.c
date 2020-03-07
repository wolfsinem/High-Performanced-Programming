/* spmd.c
 * ... illustrates the single program multiple data
 *      (SPMD) pattern using basic MPI commands.
 *
 * Huib Aldewereld, HU, HPP, 2020
 *
 * Compile by: mpicc -o spmd mpispmd.c
 * Usage: mpirun -np 4 ./spmd
 *
 * brew install openmpi on mac 
 */

#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
	int id = -1, numProcesses = -1, length = -1;
	char myHostName[MPI_MAX_PROCESSOR_NAME];

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &id);
	MPI_Comm_size(MPI_COMM_WORLD, &numProcesses);
	MPI_Get_processor_name (myHostName, &length);

	printf("Greetings from process %d of %d on %s\n",
		id, numProcesses, myHostName);

	MPI_Finalize();
	return 0;
}

/* output
 * Greetings from process 0 of 1 on mbp-van-sinem.home
 * Greetings from process 1 of 2 on mbp-van-sinem.home
 * PMIX ERROR: ERROR in file gds_ds12_lock_pthread.c at line 206
 * 
 * There are not enough slots available in the system to satisfy the 4 
 * slots that were requested by the application:
 * 				./spmd
 */