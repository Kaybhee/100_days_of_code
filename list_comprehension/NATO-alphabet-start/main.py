import pandas as pd 
nato_data = pd.read_csv(r"C:\Users\HP\Videos\100_days_of_code\NATO-alphabet-start\nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a letter: ").upper()
coded_words = [nato_dict[letters] for letters in word]
print(coded_words)
