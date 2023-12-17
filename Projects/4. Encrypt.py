# getting inputs in a list to access each element
import random
p = input('enter encryption key\n')

# modifying the key
p = str((int(p) * random.randint(1, 9) - 9873 + random.randint(50, 100) * random.choice([2, 4, 6, 8])))
p = str(p)

# removing zero because zero will give error when decrypting
k = []
for char in p:
    if char == '0':
        char = random.randint(1, 9)
    k.append(char)
# print(k)

key = [int(l) for l in k]

message = input('enter message\n')
msg = [l for l in message]

# encryption algorithm
x = -1
encrypted = []
for i in range(len(msg)):
    x = x + 1
    if x > len(key)-1:
        x = 0
    asc = ord(msg[i])  # returns ascii code of a character
    temp = key[x]
    encrypted.append(chr(asc + temp))  # chr() returns ch when ascii is passed

# printing encrypted message
print('Encrypted Messsage: ', end='')
for ch in encrypted:
    print(ch, end='')

# generate a decryption key
decrypt_key = []
for element in key:
    decrypt_key.append(element - element * 2)

# print decryption key
print('\nDecryption Key:', end='')
for g in decrypt_key:
    print(g, end='')


# -6-2-3-2-6-2-6-6-9-5-8-2-3
# s{#pgok&rx(wvgkp