# __author__ = "Shubham Srivastava"
# """
# Purpose : Multiprocessing based on inputs
# """
#
# from multiprocessing import Pipe, Process
#
# def multiprocessing_function(function_name, **input_dict):
#
#     list_of_pin_codes = input_dict["list_of_pin_codes"]
#
#     # Multiprocessing logic
#     # create a list to keep all processes
#     processes = []
#
#     # create a list to keep connections
#     parent_connections = []
#
#     # create a process per pin code
#     for pin_code in list_of_pin_codes:
#         # create a pipe for communication
#         parent_conn, child_conn = Pipe()
#         parent_connections.append(parent_conn)
#
#         # create the process,trigger get_info function pass arguements and connection
#         process = Process(target=function_name, args=(pin_code, child_conn))
#         processes.append(process)
#
#     # start all processes
#     for process in processes:
#         process.start()
#
#     # make sure that all processes have finished
#     for process in processes:
#         process.join()