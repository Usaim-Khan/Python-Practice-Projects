import math
import random

lb = int(input('enter lower bound:'))
ub = int(input('enter upper bound:'))

max_guesses = round(math.log(ub - lb +1,2))
secret_num = random.randint(lb,ub)
# print('Number is generated')
# print(f'you have {max_guesses} chances to guess the number')
count = 0
flag = False

while True:
    print(f'you have {max_guesses-count} chances left to guess the number ')
    guess = int(input('\nEnter Your Guess:'))
    count += 1
    if guess == secret_num:
        flag = True
        break
    if count == max_guesses:
        break
    if guess > secret_num:
        print('Your guess is too high')
    elif guess< secret_num:
        print('Your guess is too low')

if flag:
    print(f'Congrats! You guessed the number in {count} tries')
else:
    print('You were unable to guess the number')