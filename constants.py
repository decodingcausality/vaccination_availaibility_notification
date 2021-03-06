# headers = {
#     'authority': 'scrapeme.live',
#     'dnt': '1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'none',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# }

headers = {"accept" : "application/json", "Accept-language": "hi_IN", "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"

FIND_BY_PIN_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="
FIND_BY_STATE_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"
FIND_BY_DISTRICT_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="
GET_STATES_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/admin/location/states"