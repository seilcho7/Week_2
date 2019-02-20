letters = 'abcdefghijklmnopqrstuvwxyz'
secret = 'bad'

def convert_letter_to_number(a_letter, master):
    # find a_letter in master
    return master.index(a_letter)
    # save the index
    # then return it

print(convert_letter_to_number('b', letters))
# [1]
print(convert_letter_to_number('a', letters))
# [0]
print(convert_letter_to_number('d', letters))
# [3]

def map_over(collection, master, do_translation):
    result = []
    for letter in collection:
        result.append(do_translation(letter, master))
    return result

# for each item in a string sequence, translate to numbers
def encode(message, master):
    return map_over(message, master, convert_letter_to_number)
    # result = []
    # for letter in message:
    #     result.append(convert_letter_to_number(letter, master))
    # return result

print(encode(secret, letters))