# Monoalphabetic-Cipher Program

def main():
    key = 'Computer'
    print(' Keyword: ')

    encoded = encoder(key);

    message = 'Subject Name is Cryptography'
    print(' Message before Ciphering:-\n ', message)

    print(' Ciphered Text:-\n ', cipheredIt (message, encoded), '\n')


# Function generates the encoded text
def encoder (key):
    encoded = ''
    arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range (0, len(key)):
        if (key[i] >= 'A' and key[i] <= 'Z'):
            if (arr[key[i]-65] == 0):
                encoded += key[i]
                arr[key[i]-65] = 1

        elif (key[i] >= 'a' and key[i] <= 'z'):
            if (arr[key[i]-97] == 0):
                encoded += key[i] - 32
                arr[key[i]-97] = 1

        for i in range (0, 26):
            if(arr[i] == 0):
                arr[i] = 1
                encoded += char(i + 65)

    return encoded

# Function that generates encodes(cipher) the message
def cipheredIt (msg, encoded):
    cipher = ''
    pos = 0

    for i in range (0, len(key)):
        if (msg[i] >= 'a' and msg[i] <= 'z'):
            pos = msg[i] - 97
            cipher += encoded[pos]

        elif (msg[i] >= 'A' and msg[i] <= 'Z'):
            pos = msg[i] - 65
            cipher += encoded[pos]

        else:
            cipher += msg[i]

    return cipher;

main()
