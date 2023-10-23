#import random
#random_num = random.randint(0,1)
#if random_num == 1:
    ##print("Heads")
#else:
    #print("Tails")

import random
#names_string =  input("Give me everybody's names, separated by a comma.\n ")
#names = names_string.split(", ")
#name_len = len(names)
#random_names = random.randint(0, name_len - 1)
#person = names[random_names]
#print(person + " is going to pay for the meal today!") 
#random_name = random.choice(names)
#print(random_name + " will pay the bill")#
name = input("Give any string of names\n")
name_split = name.split(",")
name_len = len(name_split)
name_random = random.randint(0, name_len - 1)
person = name_split[name_random]
name_random1 = "The person who will pay is " + person
print(name_random1)
