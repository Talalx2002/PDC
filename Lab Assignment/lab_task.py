import random
import multiprocessing
import time

# Function to perform matrix-vector multiplication
def mat_vec_multiply(matrix_row, vector):
    # Convert elements to float to ensure numeric values
    return sum(x * y for x, y in zip(matrix_row, vector))

def for_map(args):
    matrix_row, vector = args
    return sum(x * y for x, y in zip(matrix_row, vector))

def apply_method(A, B, processes=4):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=processes)
    # Apply mat_vec_multiply function to each row of matrix A
    results = pool.apply_async(mat_vec_multiply, args=(A, B))
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return results.get(), execution_time

def apply_async_method(A, B, processes=4):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=processes)
    result = pool.apply_async(mat_vec_multiply, args=(A, B))
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result.get(), execution_time

def map_method(A, B, processes=4):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=processes)
    result = pool.map(for_map, [(row, B) for row in A])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def map_async_method(A, B, processes=4):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=processes)
    result = pool.map_async(for_map, [(row, B) for row in A])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result.get(), execution_time

def starmap_method(A, B, processes=4):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=processes)
    result = pool.starmap(mat_vec_multiply, [(A, b) for b in B])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def starmap_async_method(A, B, processes=4):
    start_time = time.time()
    pool = multiprocessing.Pool(processes=processes)
    result = pool.starmap_async(mat_vec_multiply, [(A, b) for b in B])
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result.get(), execution_time

if __name__ == "__main__":
    # Generate random matrix A and vector B without using NumPy
    A = [[random.random() for _ in range(200)] for _ in range(200)]
    B = [random.random() for _ in range(200)]

    # Measure execution time for each method with 4 processes
    result_apply, time_apply = apply_method(A, B, processes=4)
    result_apply_async, time_apply_async = apply_async_method(A, B, processes=4)
    result_map, time_map = map_method(A, B, processes=4)
    result_map_async, time_map_async = map_async_method(A, B, processes=4)
    result_starmap, time_starmap = starmap_method(A, B, processes=4)
    result_starmap_async, time_starmap_async = starmap_async_method(A, B, processes=4)

    # Print results
    print(f"Method: apply, Execution Time: {time_apply:.6f} seconds")
    print(f"Method: apply_async, Execution Time: {time_apply_async:.6f} seconds")
    print(f"Method: map, Execution Time: {time_map:.6f} seconds")
    print(f"Method: map_async, Execution Time: {time_map_async:.6f} seconds")
    print(f"Method: starmap, Execution Time: {time_starmap:.6f} seconds")
    print(f"Method: starmap_async, Execution Time: {time_starmap_async:.6f} seconds")
