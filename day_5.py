#To print the sum for a number in a list using for loop
highest_score = input("Input the highest number with a space\n").split()
for i in range(0, len(highest_score)):
    highest_score[i] = int(highest_score[i])
    score_int = 0
#for score in highest_score:
    #score_int += score
#print(score_int)
for score in highest_score:
    if score > score_int:
        score_int = score
print(score_int)
    
