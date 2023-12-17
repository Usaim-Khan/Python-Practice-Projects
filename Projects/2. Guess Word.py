import random
words = ['alphabet', 'idyllic', 'shop', 'planet', 'controversy', 'noise',
         'advantage','tuple','increase','betray','vegetables']
w = 'king'
# w = random.choice(words) # randomly selecting a word from list above
line = ['_' for i in range(len(w))] # showing places for alphabets

# initializing variables
chances = 5
correct = 0
wrong = 0

print('\nGuess the word by guessing 1 letter at a time'.upper())
# print(f'You have {chances} chances of guessing wrong')

word = [i for i in w] # getting string into list

while correct != len(word) and wrong < chances:
    if wrong >= chances:
        break


    print(f'\nYou have {chances - wrong} guesses left')
    for j in line:
        print(j, end='')


    guess = input('\nEnter your guess\n')
    if guess in word:
        correct += 1
        for k in range(word.count(guess)):
            index = word.index(guess)
            word[index] = '_'
            line[index] = guess

    else:
        wrong += 1
        print('Your guess is not correct')


if wrong < chances:
    print(f'YOU WON. Your {wrong} guesses were wrong')
else:
    print('YOU LOST')
    print(f'the word was \'{w}\'')