#To print an even number using the for loop 
total = 0
for i in range(1, 101, 1):
    if i % 2 == 0:
        total += i
print(total)