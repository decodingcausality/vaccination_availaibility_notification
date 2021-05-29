# vaccination_availaibility_notification


Get vaccine availaiblity information from COWIN website using Python and REST API and get a notification whenever a center has availibility in your area.

Modules Required :

Use Commands to get required modules :

pip install requests
pip install multiprocessing

There are primarly three modules.

main file : get_vaccine_info.py,configs and constants.

Optional : You would need to comment the send_sms function if not required.
Set mobile number in configs.py to get notifications on your phone number. You would need to register on TWILIO to generate SSID AND AUTH TOKEN from their website and copy them in configs file.
Link to register on TWILIO : https://www.twilio.com/docs/sms/quickstart/python

After this you can directly run the get_vaccine_info.py file and it should ask for the search based on PIN CODE or state code.


###This project is still in progress and may require modifications based on requirements.
