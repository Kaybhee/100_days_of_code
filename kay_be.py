from datetime import date

name = input("What's your name?\n") #abdulkabir

birthdate = input("What's your birthdate? (YYYY-MM-DD)\n")

birth_year, birth_month, birth_day = map(int, birthdate.split('-'))

today = date.today()
# Capture the date and birthyear to obtain the age
age = today.year - birth_year
# Print message
print(f"Happy {age}st birthday {name}, May all your dreams come true and your days be filled with love and joy") 