__author__ = "Shubham Srivastava"
"""
Purpose : Multiprocessing based on inputs
"""

from multiprocessing import Pipe, Process

def multiprocessing_function(function_name,input_list):

    # Multiprocessing logic
    # create a list to keep all processes
    processes = []

    # create a list to keep connections
    parent_connections = []

    # create a process per pin code
    for districts in input_list:
        # create a pipe for communication
        parent_conn, child_conn = Pipe()
        parent_connections.append(parent_conn)
        print(f"multiprocessing : {districts}")

        # create the process,trigger get_info function pass arguements and connection
        process = Process(target=function_name, args=(districts, child_conn))
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # make sure that all processes have finished
    for process in processes:
        process.join()