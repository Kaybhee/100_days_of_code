#project 4
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = ["33", " ", " "]
# A list in another list(Nested list)
map = [row1, row2, row3]
# To print them inorder to form 3x3 square
#print(f"{row1}\n {row2}\n {row3}")
position = input("Where do u want to print the treasure\n")

#To print a value using a two string format 23(column 2, row3)
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n {row2}\n {row3}")
