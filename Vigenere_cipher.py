# Vigenere Cipher Program

def generateKey (string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range (len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# Encryption
def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
         x = (ord(string[i]) + ord(key[i])) % 26
         x += ord('A')
         encrypt_text.append(chr(x))
    return("" . join(encrypt_text))

# Decryption
def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

# Driver Code
if __name__ == "__main__":
    string = input ("\n Enter the message:-\n  ")
    keyword = input (" Enter the keyword: ")
    key = generateKey (string, keyword)
    encrypt_text = encryption (string, key)
    print ("\n Encrypted message:-\n  ", encrypt_text)
    print (" Decrypted message:-\n  ", decryption(encrypt_text, key), '\n')
