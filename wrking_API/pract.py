import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 6.621070
MY_LONG = 3.503440


def dist_to_position():
    response = requests.get("https://api.open-notify.org/iss-now.json()")

    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # curr_date = datetime.now()
    # print(curr_date)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
            True
    False




def is_late():
    parameter = {"lat": MY_LAT,
                "lng": MY_LONG,
                "formatted": 0
                }
    response = requests.get("https://api.sunrise-sunset.org/json?", params = parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    curr_date = datetime.now().hour
    if curr_date <= sunrise or curr_date >= sunset:
        print("It is Dark")
while True:
    # time.sleep(10)
    if dist_to_position and is_late:
        try:
            MY_EMAIL = "abdulkabirbadru@gmail.com"
            PASS = 8447595537
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(email = MY_EMAIL, password= PASS)
            connection.sendmail(from_addr= MY_EMAIL, to_addrs= MY_EMAIL, msg= "Subject: Look right up \n\n The ISIS is up in the sky")
            connection.close()
        except Exception as e:
             print(f"There was an error: {e}")


#         


    # # sunrise.split("T")
    # print(sunrise)
# print(sunset)


