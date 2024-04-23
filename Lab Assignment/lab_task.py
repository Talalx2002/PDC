import numpy as np
import multiprocessing
import time

# Function to perform matrix-vector multiplication
def mat_vec_multiply(matrix_row, vector):
    return np.dot(matrix_row, vector)

def mat_vec_multiply1(args):
    matrix_row, vector = args
    return np.dot(matrix_row, vector)


# Function for multiprocessing using apply method
def apply_method(A, B):
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.apply(mat_vec_multiply, args=(A, B))
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Function for multiprocessing using apply_async method
def apply_async_method(A, B):
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.apply_async(mat_vec_multiply, args=(A, B))
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result.get(), execution_time

# Function for multiprocessing using map method
def map_method(A, B):
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(mat_vec_multiply, [(row, B) for row in A])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
    
# Function for multiprocessing using map_async method
def map_async_method(A, B):
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(mat_vec_multiply1, [(row, B) for row in A])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result.get(), execution_time

# Function for multiprocessing using starmap method
def starmap_method(A, B):
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.starmap(mat_vec_multiply, [(A, b) for b in B])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Function for multiprocessing using starmap_async method
def starmap_async_method(A, B):
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.starmap_async(mat_vec_multiply, [(A, b) for b in B])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result.get(), execution_time

if __name__ == "__main__":
    # Generate random matrix A and vector B
    A = np.random.rand(200, 200).astype(np.float32)
    B = np.random.rand(200).astype(np.float32)

    # Measure execution time for each method
    result_apply, time_apply = apply_method(A, B)
    result_apply_async, time_apply_async = apply_async_method(A, B)
    result_map, time_map = map_method(A, B)
    result_map_async, time_map_async = map_async_method(A, B)
    result_starmap, time_starmap = starmap_method(A, B)
    result_starmap_async, time_starmap_async = starmap_async_method(A, B)

    # Print results
    print(f"Method: apply, Execution Time: {time_apply:.6f} seconds")
    print(f"Method: apply_async, Execution Time: {time_apply_async:.6f} seconds")
    print(f"Method: map, Execution Time: {time_map:.6f} seconds")
    print(f"Method: map_async, Execution Time: {time_map_async:.6f} seconds")
    print(f"Method: starmap, Execution Time: {time_starmap:.6f} seconds")
    print(f"Method: starmap_async, Execution Time: {time_starmap_async:.6f} seconds")
