# Mono-Alphabetic Cipher Program

keys = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n'}

def encrypt(text):
    text = str (text)
    encrypting = []
    for l in text:
        encrypting.append (keys.get (l,l))
    encrypted = str (''. join (encrypting))
    return encrypted

# Driver code
if __name__ == "__main__":
    message1 = 'Subject is Cryptography'
    encoded1 = encrypt (message1);

    print ('\n Original Message:-\n ', message1)
    print (' Message after Ciphering:-\n ', encoded1)

    message2 = 'Crypto Currency'
    encoded2 = encrypt (message2);

    print ('\n Original Message:-\n ', message2)
    print (' Message after Ciphering:-\n ', encoded2, '\n')
