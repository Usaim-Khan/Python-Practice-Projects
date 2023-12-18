import random

'''
1 Input Symbol
2 Randomly Select who will move first
3 User Moves
            3.1 Take Input of position
            3.2 Check if input is valid and possible (possible means not occupied already)
            3.3 remove the position from the list if input is possible so it can not be chosen again
            3.4 add the user symbol to the current moves list on the position selected
            
4 Check for Draw OR Win
5 Computer Moves
            5.1 Randomly Select a position from the available moves and remove it so it cant be chosen again
            5.2 add computer symbol to the current moves list on the position selected
6 Check for Draw OR Win
            6.1 Check For Draw
            6.1.1 If Winner is no one and the whole board is full then game is draw
            6.1.2 full board can be detected when available moves list have length = 0
            
            6.2 Check For Win
            6.1.2 Check for the symbols of player and computer on all rows, columns and diagonals

'''
def board(moves):
    print(f'{moves[0]}|{moves[1]}|{moves[2]}')
    print('-+-+-')
    print(f'{moves[3]}|{moves[4]}|{moves[5]}')
    print('-+-+-')
    print(f'{moves[6]}|{moves[7]}|{moves[8]}')
    print('-----------------------------')


def users_move():
    print("Player's Move\n")
    global available_moves
    global current_moves
    while True:
        player_move = int(input('enter position: O'))
        if player_move in available_moves:
            available_moves.remove(player_move)
            current_moves[player_move] = user_sign
            break
        else:
            print('This space is already used or invalid input')

def computer_move():
    print("Computer's Turn\n")
    global available_moves
    global current_moves

    comp_move = random.choice(available_moves)
    available_moves.remove(comp_move)
    current_moves[comp_move] = comp_sign

def check_draw():
    global game_over
    if game_over == False:
        if len(available_moves) == 0:

            print('Game Over')
            print('Draw')
            game_over = True
            global draw
            draw = True


def check_winner(player):
    global winner
    global game_over
    global draw
    if player == 'user':
        if ((user_sign == current_moves[0] and user_sign == current_moves[1] and user_sign == current_moves[2])  #R1
        or (user_sign == current_moves[3] and user_sign == current_moves[4] and user_sign == current_moves[5])   #R2
        or (user_sign == current_moves[6] and user_sign == current_moves[7] and user_sign == current_moves[8])   #R3
        or (user_sign == current_moves[0] and user_sign == current_moves[3] and user_sign == current_moves[6])   #C1
        or (user_sign == current_moves[1] and user_sign == current_moves[4] and user_sign == current_moves[7])   #C2
        or (user_sign == current_moves[2] and user_sign == current_moves[5] and user_sign == current_moves[8])   #C3
        or (user_sign == current_moves[2] and user_sign == current_moves[4] and user_sign == current_moves[6])   #D/
        or (user_sign == current_moves[0] and user_sign == current_moves[4] and user_sign == current_moves[8])   #D\
        ):
            winner = player
            game_over = True
            draw = False

    else:
        if ((comp_sign == current_moves[0] and comp_sign == current_moves[1] and comp_sign == current_moves[2])     # R1
            or (comp_sign == current_moves[3] and comp_sign == current_moves[4] and comp_sign == current_moves[5])  # R2
            or (comp_sign == current_moves[6] and comp_sign == current_moves[7] and comp_sign == current_moves[8])  # R3
            or (comp_sign == current_moves[0] and comp_sign == current_moves[3] and comp_sign == current_moves[6])  # C1
            or (comp_sign == current_moves[1] and comp_sign == current_moves[4] and comp_sign == current_moves[7])  # C2
            or (comp_sign == current_moves[2] and comp_sign == current_moves[5] and comp_sign == current_moves[8])  # C3
            or (comp_sign == current_moves[2] and comp_sign == current_moves[4] and comp_sign == current_moves[6])  # D/
            or (comp_sign == current_moves[0] and comp_sign == current_moves[4] and comp_sign == current_moves[8])  # D\
        ):
            winner = player
            game_over = True
            draw = False


# --------------------------------------------------------


current_moves =[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # indexing from 0
available_moves = [0,1,2,3,4,5,6,7,8]
game_over = False
draw = False
winner = ''
sample = [0,1,2,3,4,5,6,7,8]
print('The Numbering is as follows:')
board(sample)

user_sign = input('Enter your sign X or O')
if user_sign == 'X':
    comp_sign = 'O'
else:
    comp_sign = 'X'

if random.randint(0,1) == 0:
    turn = 'computer'
    print('Computer Plays First')
else:
    turn = 'player'

while not game_over:
    if turn == 'player':
        users_move()
        board(current_moves)
        turn = 'computer'
        check_winner('user')
        check_draw()
    else:
        computer_move()
        board(current_moves)
        turn = 'player'
        check_winner('computer')
        check_draw()

if winner == 'computer':
    print('You Lost')
elif winner == 'user':
    print('You Won')
elif draw:
    print('Draw')


