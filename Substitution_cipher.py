# Substitution Cipher Program
import string

# A list containing all characters
all_letters= string.ascii_letters

dict1 = {}
key = 4

for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]

plain_txt = "I am studying Data Encryption"
cipher_txt=[]

print (" Recovered Original Message:-\n ", plain_txt)

# loop to generate ciphertext

for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp =char
        cipher_txt.append(temp)

cipher_txt= "".join(cipher_txt)
print(" Cipher Text is:-\n ",cipher_txt)

dict2 = {}
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]

# loop to recover plain text
decrypt_txt = []

for char in cipher_txt:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

decrypt_txt = "".join(decrypt_txt)

print (" Recovered Original Message:-\n ", decrypt_txt, "\n")
