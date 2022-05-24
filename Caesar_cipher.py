# Caesar-Cipher Program

def Caeser_Encrypt (string, shift_num):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher += char
    elif  char.isupper():
      cipher += chr((ord(char) + shift_num - 65) % 26 + 65)
    else:
      cipher += chr((ord(char) + shift_num - 97) % 26 + 97)

  return cipher

text = input ("\n Enter the String/Phrase (for Encryption): ")
sn = int (input (" Enter the Shift-number: "))
print ("\n Original String/Phrase:-\n ", text)
print (" After Encryption:-\n ", Caeser_Encrypt (text, sn), '\n')
