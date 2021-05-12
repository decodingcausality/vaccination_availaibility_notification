"""
Problem is that each of the individual wants an automated trigger whenever there is a slot for that date and pin code.




"""


response = {
   "sessions":[
      {
         "center_id":561135,
         "name":"MLN Hospital 01",
         "address":"MLN Hospital 01",
         "state_name":"Uttar Pradesh",
         "district_name":"Prayagraj",
         "block_name":"DHQ Prayagraj",
         "pincode":211006,
         "from":"10:00:00",
         "to":"16:00:00",
         "lat":25,
         "long":81,
         "fee_type":"Free",
         "session_id":"3daf22c3-fdef-45a0-adc8-9603374171db",
         "date":"11-05-2021",
         "available_capacity":2,
         "fee":"0",
         "min_age_limit":45,
         "vaccine":"COVAXIN",
         "slots":[
            "10:00AM-11:00AM",
            "11:00AM-12:00PM",
            "12:00PM-01:00PM",
            "01:00PM-04:00PM"
         ]
      }
   ]
}
"""
Purpose : Multiprocessing based on inputs 
"""

function_name = get_info


##multiprocessing logic
# create a list to keep all processes
processes = []

# create a list to keep connections
parent_connections = []

# create a process per pin code
for pin_code in list_of_pin_codes :

   # create a pipe for communication
   parent_conn, child_conn = Pipe()
   parent_connections.append(parent_conn)

   # create the process,trigger get_info function pass arguements and connection
   process = Process(target=function_name,args=(pin_code, child_conn))
   processes.append(process)

# start all processes
for process in processes:
   process.start()

# make sure that all processes have finished
for process in processes:
   process.join()





