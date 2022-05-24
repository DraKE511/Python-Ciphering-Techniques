# Vernam Cipher Program

def Vernam (Plain, Key, Flag):
    result=""
    for i in range (len(Plain)):
        char = Plain[i]
        if (Flag):
            result += chr ((ord(char)- 97 + ord (Key[i]) - 97) % 26 + 97)
        else:
            result += chr ((ord(char) - ord (Key[i])+26) % 26 + 97)
    return result
# For simplicity, here we are only considering lowercase-values and without spaces

# Driver Code
if __name__ == "__main__":
    Plain = ''. join (input ("\n Enter the Message (Plain-text):-\n "). lower(). split())
    Key = ''. join (input (" Enter Key: "). lower(). split())
    if (len(Key) != len(Plain)):
        print (" Invalid Key!")
        exit (None)
    CipherText = Vernam (Plain, Key, True)
    print (" Encrypted Message (Cipher-Text):-\n ", CipherText)
    print (" Decrypted/Original Message:-\n ", Vernam (CipherText, Key, False), '\n')
