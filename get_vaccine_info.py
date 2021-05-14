__author__ = "Shubham Srivastava / DecodingCausality"

"""
Purpose :   To fetch info for vaccine availability based on state code
Input   :   PIN CODE, Date 
Output  :   Fetch available shots for each center and if shots are available then pushing a notification on mail/contact number
"""

# Import modules
import requests
import constants
import config
import time
import datetime
import send_sms
import pprint
import multiprocessing_module

#Generate Execution Date
date = datetime.date.today().strftime("%d-%m-%Y")

def get_user_inputs(date):

    # input("Please enter mobile number on which you would like to get notified")

    print(f"***********************************Getting Vaccination Info********************************************")

    option = input("""Would you Like to Search by entering PIN CODE or selecting from available STATES ? 
    IF PINCODE then enter 1 or for STATE enter 2 : """)
    if option == str(1) :

        # Get user inputs for PIN code based search
        pin_code = input("Please enter PIN CODE ")

        available_capacity, min_age_limit, name, address = get_info_for_pin_code(pin_code, date)

        return option,pin_code,available_capacity,min_age_limit,name,address

    elif option == str(2):
        #   logic for Searching based on State
        print(f"***************Getting States with their State IDs")
        response_all_states = requests.get(url=constants.GET_STATES_ENDPOINT, headers=constants.headers)
        response_all_states = response_all_states.json()
        total_states = len(response_all_states['states'])
        print(f"Total States : {total_states}")
        for i in range(total_states) :
            state_id = response_all_states['states'][i]['state_id']
            state_name = response_all_states['states'][i]['state_name']
            print(f"State Name : {state_name}, State ID : {state_id} ")


        #Get Input for State ID from User
        state_id = input("Enter State ID : ")
        #get response for states

        # # Request URL For State ID Search
        request_url_state = f"{constants.FIND_BY_STATE_ENDPOINT}{state_id}"

        response_state = requests.get(url = request_url_state, headers=constants.headers)
        print(f"Response received for state : {response_state}")
        status_code = response_state.status_code
        print(f"status_code {status_code}")
        if status_code ==  200 :
            response_state = response_state.json()
            total_districts = len(response_state['districts'])
            print(f"Total Number of Vaccination center for State Code : {config.state_id} are {total_districts}")
            district_id_list = []
            for i in range(total_districts) :
                district_id = response_state['districts'][i]['district_id']
                district_name = response_state['districts'][i]['district_name']
                print(f"district ID : {district_id} : District Name : {district_name}")

                district_id_list.append(district_id)

        district_id_user = input("Enter District ID to initiate a search : ")

        pin_code = ""
        return option,pin_code,district_id_user,district_id_list

def get_info_for_pin_code(pin_code,date):

    request_url_pin = f"{constants.FIND_BY_PIN_ENDPOINT}{pin_code}&date={date}"

    # Get request for slot availability based on pin
    response_pin = requests.get(url = request_url_pin, headers=constants.headers)
    status_code = response_pin.status_code

    response = response_pin.json()
    response = dict(response)
    sessions = response["sessions"]
    avaiable_centers = len(sessions)

    print(f"Number of available centers are : {avaiable_centers}")
    # initialize a counter
    counter = 0
    for centers in sessions:

        counter = counter + 1
        center_id = centers["center_id"]
        name = centers["name"]
        address = centers["address"]
        state_name = centers["state_name"]
        district_name = centers["district_name"]
        block_name = centers["block_name"]
        pincode = centers["pincode"]
        vaccine = centers["vaccine"]
        fee_type = centers["fee_type"]
        slots = centers["slots"]
        min_age_limit = centers["min_age_limit"]
        date = centers["date"]
        available_capacity = centers["available_capacity"]

        print(f"**********************************************Center number : {counter}")
        print(f"The center ID is : {center_id}")
        print(f"Name of Hospital : {name}")
        print(f"The location of centre : {address} ")
        print(f"The name of state : {state_name}")
        print(f"The block name is : {block_name}")
        print(f"The Pincode : {pincode}")
        print(f"The available vaccine is : {vaccine}")
        print(f"Fee Type  : {fee_type}")
        print(f"Available slots : {slots}")
        print(f"Minimum age limit : {min_age_limit}")
        print(f"Date on which request has been made or checked : {date}")
        print(f"Available capacity : {available_capacity}")

        if min_age_limit == 18 :
            print(f"Shots available for 18 + range of age group : {available_capacity}")
            print(f"###############################@@@@@@Shots available for 18 + range of age group : {available_capacity}")
            # Set Availaibility Flag to true
            available_flag = True
            # set age group flag
            age_group = "18+"
            return available_flag, age_group,option,pin_code,available_capacity,min_age_limit,name,address

        elif min_age_limit == 45:
            print(f"Shots available for 45 +  : {available_capacity}")
            available_flag = True
            # set age group flag
            age_group = "45+"
            return available_flag, age_group,option,pin_code,available_capacity,min_age_limit,name,address

    return available_capacity, min_age_limit ,name, address,available_flag, age_group


def set_flags(available_capacity, min_age_limit):
    #notification flag for 18 and above :
    # Default Flags
    available_flag = False
    if min_age_limit < 45 and available_capacity > 0:
        print(f"###############################@@@@@@Shots available for 18 + range of age group : {available_capacity}")
        # Set Availaibility Flag to true
        available_flag = True
        # set age group flag
        age_group = "18+"
        return available_flag, age_group
    elif min_age_limit == 45 and available_capacity > 0:
        print(f"Shots available for 45 +  : {available_capacity}")
        available_flag = True
        # set age group flag
        age_group = "45+"
        return available_flag, age_group
    else:
        print("error fetching data")

def fetch_data_district_id(district_id,child_conn) :
    # Generate Execution Date
    date = datetime.date.today().strftime("%d-%m-%Y")
    # Generate request url for district code
    request_url_district = f"{constants.FIND_BY_DISTRICT_ENDPOINT}{district_id}&date={date}"
    # get response for district
    response_district = requests.get(url=request_url_district, headers=constants.headers)
    status_code = response_district.status_code
    response_district = response_district.json()
    response = dict(response_district)
    sessions = response["sessions"]
    avaiable_centers = len(sessions)

    print(f"Number of available centers are : {avaiable_centers}")
    # initialize a counter
    counter = 0
    for centers in sessions:
        counter = counter + 1
        center_id = centers["center_id"]
        name = centers["name"]
        address = centers["address"]
        state_name = centers["state_name"]
        district_name = centers["district_name"]
        block_name = centers["block_name"]
        pincode = centers["pincode"]
        vaccine = centers["vaccine"]
        fee_type = centers["fee_type"]
        slots = centers["slots"]
        min_age_limit = centers["min_age_limit"]
        date = centers["date"]
        available_capacity = centers["available_capacity"]

        print(f"**********************************************Center number : {counter}")
        print(f"The center ID is : {center_id}")
        print(f"Name of Hospital : {name}")
        print(f"The location of centre : {address} ")
        print(f"The name of state : {state_name}")
        print(f"The block name is : {block_name}")
        print(f"The Pincode : {pincode}")
        print(f"The available vaccine is : {vaccine}")
        print(f"Fee Type  : {fee_type}")
        print(f"Available slots : {slots}")
        print(f"Minimum age limit : {min_age_limit}")
        print(f"Date on which request has been made or checked : {date}")
        print(f"Available capacity : {available_capacity}")
        pin_code = ""

        if min_age_limit == 18 and available_capacity > 0:
            print(f"########################################## {center_id},{name},{address},{pincode}")
            exit()
            break
        elif min_age_limit == 45 and available_capacity > 0:
            print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% {center_id},{name},{address},{pincode}")
    print(f"***********************************************{min_age_limit}")
    child_conn.close()






# Driver Code
if __name__ == '__main__':
    option,pin_code,district_id_user,district_id_list = get_user_inputs(date)
    while True :
        multiprocessing_module.multiprocessing_function(fetch_data_district_id, district_id_list)
            # fetch_data_district_id(district_id, date)




