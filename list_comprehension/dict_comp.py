sentence = "What is the Airspeed velocity of an unladen Swallow"
sentence_split = sentence.split()
result = {
    letters: len(letters) for letters in sentence_split 
} 




print(result)