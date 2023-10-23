alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type ypur message: \n").lower()
shift = int(input("Type the shift number: \n"))

# create a function called 'encrypot' function that takes the 'text' and 'shift' as inputs
# inside the encrypt function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
# call the function   
    
def encrypt(text_1, shift_1):
    cypher_text = " "
    for letter in text_1:
        position = alphabet.index(letter)
        position_shift = position + shift_1
        position_shift1 = alphabet[position_shift]
        cypher_text += position_shift1
    print(f"The alphabet of the position difference is {cypher_text}")
# To decrypt the function
def decrypt(text_1, shift_1):
# To decide if the position chosen was encode or decrypt
    cypher_text = " "
    for letter in text_1:
        position = alphabet.index(letter)
        position_shift = position - shift_1
        new_position = alphabet[position_shift]
        cypher_text += new_position
    print(f"The alphabet of the position diffference is {cypher_text}")


#To determine if it is 'decrypt' or 'encrypt'
if direction == "encode":
    encrypt(text_1 = text, shift_1 = shift)
elif direction == "decode":
    decrypt(text_1 = text, shift_1 = shift)
else:
    print(direction)
