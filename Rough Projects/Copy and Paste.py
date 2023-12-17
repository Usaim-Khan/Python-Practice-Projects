import pyperclip


x = pyperclip.paste()  # x has data
lines = x.split('\n',)  # split when \n is found
# print(lines)

for i in range(len(lines)):
    lines[i] = '* '+ lines[i]   # add star



result = '\n'.join(lines)
# print(result)
pyperclip.copy(result)
