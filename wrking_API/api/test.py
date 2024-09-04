import requests
open_notify_api = "http://api.open-notify.org/iss-now.json"

def dist_to_position():
    response = requests.get(open_notify_api)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # curr_date = datetime.now()
    # print(curr_date)
    MY_LAT = 6.621070
    MY_LONG = 3.503440

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5<= iss_longitude <= MY_LONG + 5:
        True
    False


dist_to_position()