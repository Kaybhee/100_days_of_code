student_dict = {
    "name": ["Azeez","Kabir", "Rahman","Rahmat"],
    "Score": [21,30,26,19]
}
for(key, value) in student_dict.items():
    print(value)
import pandas as pd
new_data = pd.DataFrame(student_dict)
#The iterrows() method to loop through a dataframe
for (key, row) in new_data.iterrows():
    print(key)
    if row.name == "Azeez":
        print(row.Score)