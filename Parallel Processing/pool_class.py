from multiprocessing import Pool 
import time

def f(x): 
    return x*x 

def z(x, y): 
    return x*y 

def y(matrix_tuple):
    matrix, x = matrix_tuple
    return matrix * x

if __name__ == '__main__': 
    start_time = time.time()  # Start the timer
    pool = Pool (processes=4) 
    for x in range (30000): 
        pool.apply(f, (x,))
    end_time = time.time()  # End the timer
    print("Execution time with apply:", end_time - start_time, "seconds")


if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]  # Example matrix

    start_time = time.time()  # Start the timer
    pool = Pool(processes=4)
    for x in range(30000):
        pool.map(y, ((matrix, x),))  # Note the extra comma to make it a tuple
    pool.close()
    pool.join()
    end_time = time.time()  # End the timer

    print("Execution time with map:", end_time - start_time, "seconds")

if __name__ == '__main__': 
    start_time = time.time()  # Start the timer
    pool = Pool (processes=4) 
    for x in range(30000):
        pool.map_async(y, ((matrix, x),))  # Note the extra comma to make it a tuple
    pool.close()
    pool.join()
    end_time = time.time()  # End the timer
    print("Execution time with map_async:", end_time - start_time, "seconds")


if __name__ == '__main__': 
    start_time = time.time()  # Start the timer
    pool = Pool (processes=4) 
    pool.starmap(z, [(x, x+1) for x in range(30000)])
    end_time = time.time()  # End the timer
    print("Execution time with starmap:", end_time - start_time, "seconds")

    start_time = time.time()  # Start the timer
    pool.starmap_async(z, [(x, x+1) for x in range(30000)])
    pool.close()
    pool.join()
    end_time = time.time()  # End the timer
    print("Execution time with starmap_async:", end_time - start_time, "seconds")