from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_manager():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    pass_numbers = [random.choice(numbers) for i in range(random.randint(2 ,4))]
    pass_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    pass_manager = pass_letters + pass_numbers + pass_symbols
    random.shuffle(pass_manager)
    password = "".join(pass_manager)
    pass_code_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def user_details():
    website = web_view_entry.get()
    mail_user = details_entry.get()
    password = pass_code_entry.get()
    if len(website)== 0 or len(password) == 0:
        messagebox.showinfo("Wrong entry", "Make sure you don't leave any fields empty")
    else:
        cont = messagebox.askokcancel("Password Manager", f"Is it okay to continue:\n Website: {website}\nE-mail:{mail_user}\nPassword: {password}")
        if cont:
        #Add file using append mode
            with open( "user_info.txt", "a" ) as file:
                file.write(f" {website} | {mail_user} | {password} \n" )
            web_view_entry.delete(0, END)
            pass_code_entry.delete(0, END)
        print("User details submitted successfully")
    # 

    

# ---------------------------- UI SETUP ------------------------------- #


rt = Tk()
rt.title("Password Manager")


canvas = Canvas(width = 200, height = 200)
rt.config(padx = 20, pady = 20)
password_manager = PhotoImage(file = r"C:\Users\Badru\Videos\100_days_of_code-1\262_password-manager-start\logo.png")
canvas.create_image(100,100, image= password_manager)
# canvas.pack()
canvas.grid(row =0, column = 1)
web_view = Label(text= 'website:')
details = Label(text = 'Email/Username:')
pass_code = Label(text = 'Password:')
web_view.grid(row = 1, column = 0)
details.grid(row = 2, column = 0)
pass_code.grid(row=3, column = 0)

#Create entries
web_view_entry= Entry(width = 35)
web_view_entry.grid(column = 1, row = 1, columnspan=2)
web_view_entry.focus()
details_entry = Entry(width=35)
details_entry.grid(column =1, row=2, columnspan=2)
pass_code_entry = Entry(width = 25)
pass_code_entry.grid(column =1, row= 3)

# Create Buttons
gen_password_button = Button(text = "Generate Password", command = pass_manager)
gen_password_button.grid(column=3, row=3)
add_button = Button(text =" add", width=36, command = user_details)
add_button.grid(column=1, row=4, columnspan=2 )


 
rt.mainloop()