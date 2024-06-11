# Import necessary libraries
import numpy as np
from mpi4py import MPI
import time

# Function to generate random square matrices
def generate_matrices(N):
    A = np.random.randint(10, size=(N, N))
    B = np.random.randint(10, size=(N, N))
    return A, B

# Function to perform sequential matrix multiplication
def sequential_matrix_multiplication(A, B):
    N = A.shape[0]
    C = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Function to perform local matrix multiplication
def local_matrix_multiplication(A, B, rows):
    N = A.shape[1]
    C_local = np.zeros((rows, N), dtype=int)
    for i in range(rows):
        for j in range(N):
            for k in range(N):
                C_local[i][j] += A[i][k] * B[k][j]
    return C_local

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Matrix size
N = 100  # Change as needed

# Process 0 generates the matrices
if rank == 0:
    A, B = generate_matrices(N)
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
else:
    A = None
    B = None



# Perform mpi matrix multiplication for comparison
start_time = time.time()
    

# Scatter rows of A among all processes
rows_per_process = N // size
A_local = np.zeros((rows_per_process, N), dtype=int)
comm.Scatter(A, A_local, root=0)

# Broadcast B to all processes
B = comm.bcast(B, root=0)

# Each process prints its received portion of A and B
print(f"Process {rank} received portion of A:")
print(A_local)
print(f"Process {rank} received B:")
print(B)

# Perform local matrix multiplication
C_local = local_matrix_multiplication(A_local, B, rows_per_process)

# Each process prints its resulting local matrix
print(f"Process {rank} local result C:")
print(C_local)

# Reduce the local matrices to form the final result matrix C at root process
C = None
if rank == 0:
    C = np.zeros((N, N), dtype=int)

comm.Reduce(C_local, C, op=MPI.SUM, root=0)

# Process 0 prints the final result
if rank == 0:
    print("Resulting Matrix C from parallel computation:")
    end_time = time.time()
    print("Resulting Matrix C from mpi computation:")
    print(C)
    print(f"mpi computation time: {end_time - start_time} seconds")

    # Perform sequential matrix multiplication for comparison
    start_time = time.time()
    C_seq = sequential_matrix_multiplication(A, B)
    end_time = time.time()
    print("Resulting Matrix C from sequential computation:")
    print(C_seq)
    print(f"Sequential computation time: {end_time - start_time} seconds")

# Note: Performance analysis requires running the code with different matrix sizes and number of processes