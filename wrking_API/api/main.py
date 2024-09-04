import requests
response = requests.get(url= "http://api.open-notify.org/iss-now.json")
print(response.status_code)
data= response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
data1 = (longitude, latitude)
print(data1)

import random
from tkinter import *


def get_quote():
    u_link = "https://api.kanye.rest/"
    response = requests.get(u_link)
    response.raise_for_status()
    data = response.json()
    rand_quotes = data["quote"]
    canvas.itemconfig(quote_text, text = rand_quotes)
    


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"C:\Users\Kaybee\Videos\100_days_of_code\wrking_API\api\005 kanye-quotes-start\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"C:\Users\Kaybee\Videos\100_days_of_code\wrking_API\api\005 kanye-quotes-start\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()