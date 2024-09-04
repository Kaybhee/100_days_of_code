def leapyear(year):
    if year % 4 == 0:
         if year % 100  == 0:
             if year % 400 == 0:
                 print("leap year")  
             else:
                 print("Not a leap year")
         else:
             print("leap year")
    else:
        print("Not a leap year")

def days_in_month(chosen_year, chosen_month):
    month_days = ["31","28","31","30","31","30","31","31","30","31","30","31"]
    days_output =  len(month_days) - 1
    num_days = month_days[month - 1]
    print(num_days)
year = int(input("Enter a year: "))
month = int(input("Enter the month: "))
days_in_month(chosen_year = year,chosen_month =  month)