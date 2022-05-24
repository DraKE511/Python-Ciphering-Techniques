def encryptRailFence (text, key):
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range (key):
        for j in range (len(text)):
            if rail[i][j] != '\n':
                result. append (rail[i][j])
    return ("". join (result))

def decryptRailFence (cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range (key):
        for j in range (len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range (len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return ("".join(result))

# Driver code
if __name__ == "__main__":
    message1 = 'attack at once'
    key1 = 2
    cipher1 = encryptRailFence (message1, key1)
    print ('\n Message before Ciphering:-\n ', message1)
    print (' Key used:', key1)
    print (' After Ciphering:-\n ', cipher1)
    print (' Again, after Deciphering with same Key:-\n ', decryptRailFence (cipher1, key1))

    message2 = 'defend the east wall'
    key2 = 3
    cipher2 = encryptRailFence (message2, key2)
    print ('\n Message before Ciphering:-\n ', message2)
    print (' Key used:', key2)
    print (' After Ciphering:-\n ', cipher2)
    print (' Again, after Deciphering with same Key:-\n ', decryptRailFence (cipher2, key2), '\n')
