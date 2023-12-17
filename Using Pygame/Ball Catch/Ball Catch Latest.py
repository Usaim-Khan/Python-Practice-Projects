# best one rn
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
game_window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Ball Catch')
img = pygame.image.load('ball icon.jpg')
pygame.display.set_icon(img)


def gameplay():
    game_over = False
    game_exit = False
    score = 0
    broken = True
    H_start = 720
    H_end = 870
    clock = pygame.time.Clock()
    new_value = 0

    generate_new = True
    lives = 3
    key_press_time = 0
    c_time = 0

    while not game_exit:
        if broken:
            myfile = open('ball hi scr.txt', 'r')
            for line in myfile:
                highest = line
            myfile.close()
        if game_over:
            generate_new = False
            game_window.fill(white)
            show_score2('Game Over', black, 500, 350)
            show_score2(f'Your Score {score}', red, 500, 430)
            show_score('Press Enter To Play Again',blue,500,550)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameplay()
        else:
            if generate_new:
                circle_x = random.randint(10, 1590)
                circle_y = 10
                catch = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                new_value, left, right  =  handling_input(event)

            # when to move the basket
            if H_start > 0 and H_end < 1600:
                H_start += new_value
                H_end += new_value
            else:
                if H_start == 0 and right:
                    H_start += new_value
                    H_end += new_value
                if H_end == 1600 and left :
                    H_start += new_value
                    H_end += new_value

            game_window.fill(white)
            show_score(f'Score: {score}', red, 10, 10)
            show_score(f'Lives: {lives}', green, 1420, 10)

            if score > int(highest):
                show_score(f'Highest Score: {score}', blue, 8, 55)
            else:
                show_score(f'Highest Score: {highest}', blue, 8, 55)

            if circle_y < 904:
                pygame.draw.circle(game_window, red, (circle_x, circle_y), 10)
                circle_y += 3
                generate_new = False
            else:
                generate_new = True

            if circle_x > H_start and circle_x < H_end and circle_y == 901:
                score = score + 10

            if circle_y == 901:
                if circle_x < H_start or circle_x > H_end:
                    lives -= 1

            if lives == 0:
                game_over = True

            if score > int(highest):
                broken = True
                myfile = open('ball hi scr.txt', 'w')
                myfile.write(str(score))

            create_basket(H_start, H_end)
            clock.tick(200)
            pygame.display.update()


def handling_input(event):
    left = False
    right = False
    new_value = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            left = True
            right = False
            new_value = -5
        if event.key == pygame.K_RIGHT:
            right = True
            left = False
            new_value = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left = False
            if right:
                new_value = 5
        if event.key == pygame.K_RIGHT:
            right = False
            if left:
                new_value = -5

    return new_value,left,right


def create_basket(H_start, H_end):
    pygame.draw.line(game_window, black, (H_start, 900), (H_end, 900), 20)  # horizontal line
    pygame.draw.line(game_window, black, (H_end, 900), (H_end, 870), 10)  # right vertical
    pygame.draw.line(game_window, black, (H_start, 900), (H_start, 870), 10)  # left vertical


def show_score(text, color, pos_x, pos_y):
    font = pygame.font.SysFont('serif', 50, italic=True)
    value = font.render(text, True, color)
    game_window.blit(value, [pos_x, pos_y])


def show_score2(text, color, pos_x, pos_y):
    font = pygame.font.SysFont('serif', 100, italic=True, bold=True)
    value = font.render(text, True, color)
    game_window.blit(value, [pos_x, pos_y])




gameplay()

