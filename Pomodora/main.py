
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = ""

from tkinter import *
import math
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(time)
    canvas.itemconfig(timer, text = "00:00")
    title_label.config(text = "Timer")
    markers.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec =  SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_time(long_break_sec)
        title_label.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_time(short_break_sec)
        title_label.config(text = "Break", fg = PINK)
    else:
        count_time(work_sec)
        title_label.config(text = "Work", fg = GREEN)

   
   # count_time(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_time(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
   
    canvas.itemconfig(timer, text = f"{count_min}: {count_sec}")
    if count > 0:
        global time 
        time = window.after(1000, count_time, count - 1)
    else:
        timer_start()
        checks = ""
        for i in range (math.floor(reps/ 2)):
            checks += "✔"
            markers.config(text = checks )




window = Tk()
window.title("Pomodoro")
title_label = Label(text = "Timer",bg = YELLOW, fg = GREEN, font = (FONT_NAME, 35, "bold"))
title_label.grid( column = 1, row = 0)
window.config(padx = 103, pady = 35, bg= YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW , highlightthickness= 0)
# ---------------------------- UI SETUP ------------------------------- #
tomato_png = PhotoImage(file =r"C:\Users\Badru\Videos\100_days_of_code-1\Pomodora\tomato.png" )
canvas.create_image(100, 112, image = tomato_png)
timer = canvas.create_text(103,130, text = "00:00", fill= "white", font = (FONT_NAME, 40, "bold"))

canvas.grid(column = 1, row = 1)
start_button = Button(text = "Start", highlightthickness= 0, command= timer_start)

start_button.grid(column = 0, row = 2)

reset_button = Button(text = "reset", highlightthickness= 0, command = reset_time)
reset_button.grid(column= 2, row = 2)


markers = Label(fg=GREEN, highlightthickness=0, font= (FONT_NAME,20, "bold"))
markers.grid(column = 1, row = 3)

window.mainloop()