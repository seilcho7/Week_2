letters = 'abcdefghijklmnopqrstuvwxyz'

secret = [1, 0, 3] # "bad"

word = 'bad'

def translate(index, master_list):
    return master_list[index]

def map_over(collection, master_list, how):
    result = ''
    for item in collection:
        result += how(item, master_list)

    return result

# give your functions "verb" names
def decode(number_list, master_list):
    return map_over(number_list, master_list, translate)
    # configuration came in as arguments
    # result = ''
    # count = 0

    # do the translation
    # for each item in number_list...
    # for item in number_list:

    # find that index in master_list...
        # letter = master_list[item]
    
    # put that character in result
    # result = result + letter
        # result += letter
        # result += translate(item, master_list)

    # return the result
    # return result

# decoded_message = decode(secret, letters)
print(decode(secret, letters))

def decode_while(number_list, master_list):
    result = ''
    count = 0
    max_length = len(number_list)
    while count < max_length:
        # item = number_list[count]
        # result += master_list[item]
        result += master_list[number_list[count]]
        count += 1
    
    return result

print(decode_while(secret, letters))

print(map_over(secret, letters, translate))

def encode(word, master_list):
    secret_number = []
    for item in word:
        if item in master_list:
            secret_number.append(master_list.index(item))
    return secret_number

print(encode(word, letters))