# # def even_odd_encrypt(phrase: str):
# for i in range(2, 18, 2):
#     # print(i)

# #         text = i.index
# #     return ""

# # even_odd_encrypt('message')
def even_odd_encrypt(phrase: str):
    # write your code here
    even_char = ""
    char_count = 0
    for char in phrase:
      if char_count % 2 == 0:
        even_char = even_char + char
    return "even_char"

even_odd_encrypt('message')