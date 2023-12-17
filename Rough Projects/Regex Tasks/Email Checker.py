import re
pattern = re.compile(r'\w+\@\w+(.com)')
email = input('enter your email\n')
result = pattern.search(email)
if result == None:
    print('invalid email')
else:
    print('valid email')
    print(result.group())