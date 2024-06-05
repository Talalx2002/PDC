#include <mpi.h>
#include <stdio.h>

// Function to calculate factorial
long factorial(int n) {
    if (n == 0) return 1;
    long result = 1;
    for (int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main(int argc, char* argv[]) {
    int rank, size, number = 5, local_result;
    long result;

    // Initialize MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 5) {
        if (rank == 0) {
            printf("This program requires exactly 5 processors.\n");
        }
        MPI_Finalize();
        return 1;
    }

    // Distribute the task
    if (rank == 0) {
        for (int i = 1; i < size; ++i) {
            MPI_Send(&number, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
        }

        // Compute factorial locally
        result = factorial(number);

        // Receive results from other nodes
        for (int i = 1; i < size; ++i) {
            MPI_Recv(&local_result, 1, MPI_LONG, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            result += local_result;
        }

        // Print result at processor 0
        printf("Processor %d: Factorial of %d is %ld\n", rank, number, result);

        // Print results at each node
        for (int i = 1; i < size; ++i) {
            MPI_Send(&result, 1, MPI_LONG, i, 0, MPI_COMM_WORLD);
        }
    } else {
        MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        local_result = factorial(number);
        MPI_Send(&local_result, 1, MPI_LONG, 0, 0, MPI_COMM_WORLD);

        // Receive final result from processor 0
        MPI_Recv(&result, 1, MPI_LONG, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Processor %d: Factorial of %d is %ld\n", rank, number, result);
    }

    // Finalize MPI
    MPI_Finalize();
    return 0;
}
