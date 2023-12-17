import re, pyperclip


data = pyperclip.paste()
# data = input('enter phone number\n')
pattern = re.compile(r'\b(\d\d\d)(-|\.| )(\d\d\d)(-|\.| )(\d\d\d\d)\b')
result = pattern.findall(data)
# print(len(result))
# print(result)
# print(result[1])

final = []

# for i in range(len(result)):
#     result[i] = list(result[i])
# print(result)
for numbers in result:
    for num in numbers:
        final.append(num)

num_string = ''.join(final)
# print(num_string)


aa = []

for i in range(0,len(num_string),12):
    temp = num_string[i:i+12]
    aa.append(temp)

# print(aa)
answer = '\n'.join(aa)
print('Phone numbers in data you provided are:')
print(answer)
pyperclip.copy(answer)
# print(final)