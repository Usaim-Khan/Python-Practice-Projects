import pygame
pygame.init()
import random


# COLORS
blue = (0, 100, 100)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# VARIABLES
game_over = False
game_exit = False
score = 0
H_start = 720
H_end = 870
clock = pygame.time.Clock()
new_value = 0
game_window = pygame.display.set_mode((1600,900))
generate_new = True
lives = 3

def create_basket(H_start,H_end):
    pygame.draw.line(game_window, black, (H_start, 900), (H_end, 900), 20) # horizontal line
    pygame.draw.line(game_window, black, (H_end, 900), (H_end, 870), 10) # right vertical
    pygame.draw.line(game_window, black, (H_start, 900), (H_start, 870), 10) # left vertical

def show_score(text,color,pos_x,pos_y):
    font = pygame.font.SysFont('serif',50,italic=True)
    value = font.render(text,True,color)
    game_window.blit(value,[pos_x,pos_y])

def show_score2(text,color,pos_x,pos_y):
    font = pygame.font.SysFont('serif',100,italic=True,bold= True)
    value = font.render(text,True,color)
    game_window.blit(value,[pos_x,pos_y])

myfile = open('ball hi scr.txt', 'r')
for line in myfile:
    highest = line
myfile.close()

while not game_exit:
    if generate_new:
        circle_x = random.randint(10, 1590)
        circle_y = 10
        catch = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
                right =False
                new_value = -5
            elif event.key == pygame.K_RIGHT:
                left = False
                right = True
                new_value = 5

     # when to move the basket
    if H_start > 0 and H_end < 1600:
        H_start += new_value
        H_end += new_value
    else:
        if H_start == 0 and right == True:
            H_start += new_value
            H_end += new_value
        if H_end == 1600 and left == True:
            H_start += new_value
            H_end += new_value

    game_window.fill(white)
    show_score(f'Score: {score}',red,10,10)
    show_score(f'Lives: {lives}',green,1420,10)
    show_score(f'Highest Score: {highest}',blue,8,55)

    if circle_y < 904:
        pygame.draw.circle(game_window, red, (circle_x, circle_y), 10)
        circle_y += 3
        generate_new = False
    else:
        generate_new = True


    if circle_x > H_start and circle_x < H_end  and circle_y == 901:
        score = score + 10

    if circle_y == 901:
        if circle_x < H_start or circle_x > H_end:
            lives -= 1
            # print('gameover')

    if lives == 0:
        game_over = True

    if game_over:
        generate_new = False
        game_window.fill(white)
        show_score2('Game Over',black,500,350)
        show_score2(f'Your Score {score}',red,500,430)


    create_basket(H_start,H_end)
    clock.tick(150)
    pygame.display.update()

if score > int(highest):
    myfile = open('ball hi scr.txt', 'w')
    myfile.write(str(score))