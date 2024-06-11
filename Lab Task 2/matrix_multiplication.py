import numpy as np
import time
from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Matrix size
N = 150  # Change this for different sizes: 100, 200, 400, 800

# Step 1: Matrix Generation
if rank == 0:
    A = np.random.randint(10, size=(N, N))
    B = np.random.randint(10, size=(N, N))
else:
    A = np.empty((N, N), dtype=int)
    B = np.empty((N, N), dtype=int)

# Step 2: Sequential Matrix Multiplication
if rank == 0:
    start_time = time.time()
    C_sequential = np.dot(A, B)
    sequential_time = time.time() - start_time
    print(f"Sequential Matrix Multiplication Time: {sequential_time} seconds")

# Step 3: MPI Scatter
local_A = np.empty((N // size, N), dtype=int)
local_B = np.empty((N // size, N), dtype=int)

# Scatter matrix A and matrix B to all processes
comm.Scatter(A, local_A, root=0)
comm.Scatter(B, local_B, root=0)

# Print received portions (for verification)
print(f"Process {rank} received portion of matrix A:\n{local_A}")
print(f"Process {rank} received portion of matrix B:\n{local_B}")

# Step 4: Matrix Multiplication
local_C = np.dot(local_A, local_B.T)  # Perform local matrix multiplication

# Print the resulting local matrix (for verification)
print(f"Process {rank} local result matrix:\n{local_C}")

# Step 5: MPI Reduce
C_parallel = None
if rank == 0:
    C_parallel = np.empty((N, N), dtype=int)

comm.Reduce(local_C, C_parallel, op=MPI.SUM, root=0)

# Print the resulting matrix C (for verification)
if rank == 0:
    print(f"Parallel Matrix Multiplication Result:\n{C_parallel}")

    # Performance Analysis
    parallel_time = time.time() - start_time
    print(f"Parallel Matrix Multiplication Time: {parallel_time} seconds")
    print(f"Speedup: {sequential_time / parallel_time}")

# Finalize the MPI environment
MPI.Finalize()
