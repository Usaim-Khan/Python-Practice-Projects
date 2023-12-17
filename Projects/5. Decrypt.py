k = input('enter decryption key\n')
key = []
for i in range(0, int(len(k)), 2):
    key.append(k[i:i+2])

message = input('enter encrypted message\n')
msg = [l for l in message]

# print(msg)
# print(key)

x = -1
encrypted = []
for i in range(len(msg)):
    x = x + 1
    if x > len(key)-1:
        x = 0
    asc = ord(msg[i])  # returns ascii code of a character
    temp = int(key[x])
    encrypted.append(chr(asc + temp))


print('Decrypted Message:', end='')
for ch in encrypted:
    print(ch, end='')
