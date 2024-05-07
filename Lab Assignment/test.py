
if _name_ == "_main_":
    
    start_time = time.time()
    C_serial = [compute_row(i) for i in range(200)]
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time using serial: {execution_time:.6f} seconds")
    
    
    
    num_processes = 4  # Adjust as needed
    start_time = time.time()
    with Pool(num_processes) as pool:
        C_parallel = pool.map(compute_row, range(200))
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time using pool.map(): {execution_time:.6f} seconds")

    
    
    start_time = time.time()
    with Pool(num_processes) as pool:
        C_parallel_map_async = pool.map_async(compute_row, range(200)).get()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time pool.map_async(): {execution_time:.6f} seconds")
    
    
    
    # Now let's compute C_parallel using pool.apply()
    C_parallel_apply = [0.0] * 200
    start_time_apply = time.time()
    with Pool(num_processes) as pool:
        for i in range(200):
            C_parallel_apply[i] = pool.apply(compute_row, args=(i,))
    end_time_apply = time.time()

    execution_time_apply = end_time_apply - start_time_apply
    print(f"Execution time using pool.apply(): {execution_time_apply:.6f} seconds")

    start_time_apply = time.time()
    with Pool(num_processes) as pool:
        C_parallel_apply_async = [pool.apply_async(compute_row, args=(i,)).get() for i in range(200)]
    end_time_apply = time.time()
    execution_time_apply_async = end_time_apply - start_time_apply
    print(f"Execution time using pool.apply_async(): {execution_time_apply_async:.6f} seconds")



    start_time_apply = time.time()
    with Pool(num_processes) as pool:
        C_parallel_starmap = pool.starmap(compute_row_starmap, [(i, A, B) for i in range(200)])
    end_time_apply = time.time()
    execution_time_astarmap = end_time_apply - start_time_apply
    print(f"Execution time using pool.starmap(): {execution_time_astarmap:.6f} seconds")


    start_time_apply = time.time()
    with Pool(num_processes) as pool:
        C_parallel_starmap_async = pool.starmap_async(compute_row_starmap, [(i, A, B) for i in range(200)]).get()
    end_time_apply = time.time()
    execution_time_starmap_async = end_time_apply - start_time_apply
    print(f"Execution time using pool.starmap_async(): {execution_time_starmap_async:.6f} seconds")
