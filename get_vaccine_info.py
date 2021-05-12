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

def get_info(date,pin_code):

    # Get pin code and date from user
    date = config.date
    pin_code = config.pin_code

    # Generate request URL based on Pin Code and Date
    request_url = f"{FIND_BY_PIN_ENDPOINT}{pin_code}&date={date}"
    print(f"Generated Request URL  vaccination availaibility in : {pin_code} and date : {date}  ******{request_url}")

    # Get request for slot availability
    response = requests.get(url = request_url, headers = constants.headers)
    response = response.json()
    response = dict(response)
    sessions = response["sessions"]
    avaiable_centers = len(sessions)

    print(f"Number of available centers are : {avaiable_centers}")
    # initialize a counter
    counter = 0
    for centers in sessions :

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
        min_age_limit =  centers["min_age_limit"]
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

        center_info = {"center_1" :{"center_id" : center_id,"name" : name,"address" : address,"state_name" : state_name,"block_name" : block_name,"pincode" : pincode,"vaccine" : vaccine,"fee_type" : fee_type,"slots" : slots,"min_age_limit" : min_age_limit,"date" : date,"available_capacity":available_capacity}}


        # notification flag for 18 and above :
        # Default Flags
        available_flag = False
        if min_age_limit < 45 and available_capacity > 0 :
            print(f"Shots available for 18 + range of age group : {available_capacity} for center {counter} ")
            # Set Availaibility Flag to true
            available_flag = True
            # set age group flag
            age_group = "18+"
            return available_flag , age_group
        elif min_age_limit == 45 and available_capacity > 0 :
            print(f"Shots available for 45 +  : {available_capacity} for center {counter}")
            available_flag = True
            # set age group flag
            age_group = "45+"
            return available_flag, age_group
        else :
            print("error fetching data")

def trigger_notification(available_flag, age_group) :

    #Redirecting to email notification function based on age group
    if available_flag == True and age_group == config.input_age_group :
        # logic to send email/sms for the user registered for that pin code
        print(f"Sending sms to the user with confirmation on : {config.target_mobile_number}")

        return constants.STATUS_SUCCESS, age_group
    else :
        return constants.STATUS_FAILED, age_group


# Driver Code
if __name__ == '__main__':
    while True :
        available_flag, age_group = get_info(config.date, config.pin_code)
        print(f"availabilty : {available_flag}, Age group : {age_group}, time : {datetime.datetime.now()}")
        status, age_group= trigger_notification(available_flag, age_group)
        #print(f"EMAIL NOTIFICATION STATUS : {status} ")
        if status == constants.STATUS_SUCCESS and age_group == config.input_age_group :
            message = send_sms.send(age_group, config.pin_code)
        time.sleep(config.interval)
