# Hill Cipher Program

keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix (key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Encryption
def encrypt (messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher (message, key):
    getKeyMatrix (key)

    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    encrypt (messageVector)

    CipherText = []
    for i in range(3):
        CipherText.append (chr (cipherMatrix[i][0] + 65))

    print (" Encrypted Message (Cipher-text):-\n ", "".join(CipherText))

# Driver Code
def main():
    message1 = "ACT"
    key1 = "GYBNQKURP"
    print ("\n Original Message:-\n ", message1)
    print (" Keyword used: ", key1)
    HillCipher (message1, key1)

    message2 = "GOD"
    key2 = "HILLYWOOD"
    print ("\n Original Message:-\n ", message2)
    print (" Keyword used: ", key2)
    HillCipher (message2, key2)
    print ('\n')

if __name__ == "__main__":
    main()
