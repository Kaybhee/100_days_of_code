alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type ypur message: \n").lower()
shift = int(input("Type the shift number: \n"))


def caesar(text_1, shift_1, direction_1):
    cypher_text = " "
    if direction_1 == "decode":
        shift_1 *= -1
    for letter in text_1:
        position = alphabet.index(letter)
        new_position = position + shift_1
        position_shift = alphabet[new_position]
        cypher_text += position_shift
    print(f"The {direction_1}d text is {cypher_text}")
caesar(text_1 = text, shift_1 = shift, direction_1 = direction)

   # elif direction == "decode":
       # for letter in text_1:
           # position = alphabet.index(letter)
           # position_shift = position - shift_1
           # new_position = alphabet[position_shift]
           # cypher_text += new_position
        #print(f"The alphabet of the position diffference is {cypher_text}")
   # else:
       # print(direction)
#caesar(text_1 = text, shift_1 = shift)



