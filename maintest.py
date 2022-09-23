import requests
from datetime import datetime
from cta_func import Cta_Func
#API_KEY = "52cf64ee9ccf4f93bf0acb17c6efdddc"
URL = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=52cf64ee9ccf4f93bf0acb17c6efdddc"
JSON_CONVERSION = "&outputType=JSON"

# Stores all stations by train color
# Use index as selectors for station
station_ID = {
    "yellow" : {"dempster-skokie": "40140", "oakton-skokie": "41680", "howard":"40900"}
    }

print("What line would you like to track")
ans = input("type 'yellow' for yellow line: ")

if ans == "yellow":
    user_stop = input("What stop: ")
    #user_stop = station_ID["yellow"][user_stop]
    for stop_name in station_ID[ans].keys():
        if stop_name == user_stop:

            response = requests.get(f"{URL}&mapid={station_ID[ans][stop_name]}{JSON_CONVERSION}").json()
            
            arrivals = response["ctatt"]["eta"]
            #stop_destination = response["ctatt"]["eta"][3]["destNm"]
            
            a = Cta_Func()
            arrival_list = a.get_arrivals(arrivals)

            # loops through list of arrivals to display est time of arrival in a readable manner  
            for dest, arr_time in arrival_list.items():
                for time in arr_time:
                    # conversion of time to 12 hour version
                    time_list = time.split("T")
                    time_list = time_list[1]
                    time_f = datetime.strptime(time_list, "%H:%M:%S").strftime("%I:%M:%S %p")
                    print(f"Train to {dest} approaching station at {time_f}")