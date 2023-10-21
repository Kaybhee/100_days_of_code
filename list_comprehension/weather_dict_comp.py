weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday":15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
result = {temp_f:(temp_c*9/5)+ 32 for (temp_f,temp_c) in weather_c.items()}
print(result)