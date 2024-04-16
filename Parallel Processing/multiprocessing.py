import multiprocessing 
from multiprocessing  import Process 

def print_func(language='Python'): 
    curr_proc = multiprocessing.current_process() 
    print('Language is ', language, "and ", curr_proc.name, "is executing this function") 


if __name__ == "__main__": 
    names = ['Python', 'Java', 'JavaScript', 'Kotlin', 'C++'] 
    procs = [] 
    # instantiating without any argument 
    proc = Process (target=print_func) 
    procs.append(proc) 
    proc.start() 
    #instantiating process with arguments 
    for name in names: 
        proc = Process (target=print_func, args=(name,)) 
        procs.append(proc) 
        proc.start() 
        # complete the processes 
    for proc in procs: 
        proc.join() 