import string

ALPHABET = string.ascii_lowercase
CHARACTERS_THAT_MUST_REMAIN_THE_SAME = string.digits + string.punctuation + string.whitespace

def cycle_get(lst,index):
    new_index = index % len(lst)
    return(lst[new_index])

def cycle_increment_index(index,lst):
    if index == len(lst) - 1:
        index = 0
    else:
        index += 1
    return(index)

def shift(letter, value):
    current_letter_value = ALPHABET.find(letter)
    end_value = current_letter_value + value
    return(cycle_get(ALPHABET,end_value))

def convert_key_to_numbers(key):
    return([ALPHABET.find(i) for i in key])

def encrypt(text, key, reverse_operation=False):
    text = text.lower()
    key = convert_key_to_numbers(key)
    index_of_key = 0
    result = ""
    for char in text:
        if char in CHARACTERS_THAT_MUST_REMAIN_THE_SAME:
            result += char
        else:
            if not reverse_operation:
                result += shift(char,key[index_of_key])
            else:
                result += shift(char,- key[index_of_key])
            index_of_key = cycle_increment_index(index_of_key,key)
    return(result)

def decrypt(text,key):
    return(encrypt(text,key,reverse_operation=True))

# Driver Code
if __name__ == "__main__":
    message1 = 'attack at once'
    key1 = 'all'
    cipher1 = encrypt (message1, key1)
    print ('\n Message before Ciphering:-\n ', message1)
    print (' Key used:', key1)
    print (' After Ciphering:-\n ', cipher1)
    print (' Again, after Deciphering with same Key:-\n ', decrypt (cipher1, key1))

    message2 = 'defend the east wall'
    key2 = 'best'
    cipher2 = encrypt (message2, key2)
    print ('\n Message before Ciphering:-\n ', message2)
    print (' Key used:', key2)
    print (' After Ciphering:-\n ', cipher2)
    print (' Again, after Deciphering with same Key:-\n ', decrypt (cipher2, key2), '\n')
