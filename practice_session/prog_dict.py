student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermoine" : 99,
    "Draco" : 74,
    "Neville" : 62
}
#print(student_scores)
student_grades = { }
#print(student_scores) 
for student in student_scores:
        # when you print student it returns the keys of the dictionary and not the values
        score = student_scores[student]
        #it returns the scores of the each student 
        #print(score)
        if score >= 91 and score <= 100:
                student_grades[student] = "Outstanding"
        elif score >= 81 and score <= 90 :
                student_grades[student] = "Exceed expectation"
        elif score >= 71 and score <= 80:
                student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"
print(student_grades)
 