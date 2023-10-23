#age = input("What is your current age?\n")
#age_int = int(age)
#age_subt = 90 - age_int
#age_subt_int = int(age_subt)
#x = age_subt_int * 365 
#y = age_subt * 52
#z = age_subt * 12
#message = f"You have {x} days, {y} weeks, and {z} months left"
#print(message)

# A tip calculator
bill = input("What is the total bill?\n")
bill_int = int(bill)
bill_tip = input("What is the percentage tip for the bill: 10,12,15?\n")
bill_tip_int = int(bill_tip)
bill_tip1 = bill_tip_int / 100
bill_split = bill_int / 5
total = bill_tip1 + bill_split
message = round(total, 2)
print(message)