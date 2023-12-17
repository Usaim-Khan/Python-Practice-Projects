import pygame
pygame.init()
import random

def show_score(text,color,pos_x,pos_y):
    font = pygame.font.SysFont('serif',30,italic=True)
    value = font.render(text,True,color)
    game.blit(value,[pos_x,pos_y])
def show_score2(text,color,pos_x,pos_y):
    font = pygame.font.SysFont('serif',100,italic=True)
    value = font.render(text,True,color)
    game.blit(value,[pos_x,pos_y])
def draw_snake(color,snake_coordinates):
    size = 12
    for x,y in snake_coordinates:
        pygame.draw.rect(game, color, [x,y, size, size])



# COLORS
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# variables


# create a game window
game = pygame.display.set_mode((800,600))
# give a name to game window
pygame.display.set_caption('Snake Game')
img = pygame.image.load('snake icon.png')
pygame.display.set_icon(img)
# colors the game window
# game.fill(white)

def gameplay():
    snake_x = 250
    snake_y = 300
    speed_x = 0
    speed_y = 0
    exit = False
    game_over = False

    clock = pygame.time.Clock()
    food_x = random.randint(5, 800)
    food_y = random.randint(5, 600)
    score = 0
    snake_list = []
    snake_size = 1
    broken = True

    while not exit:
        if broken:
            myfile = open('snk hi scr.txt')
            for line in myfile:
                highest = line
            myfile.close()
        if game_over:
            game.fill(white)
            show_score2('Game Over', red, 170, 160)
            show_score2(f'Your Score {score}',green,150,240)
            show_score('Press Enter To Play Again', blue, 240, 350)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameplay()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit = True


        else:

            snake_list.append([snake_x,snake_y])
            if len(snake_list)> snake_size:
                snake_list.pop(0)


            for event in pygame.event.get():
                # KEY HANDLING
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN: # checking if key is pressed
                    if event.key == pygame.K_RIGHT: # what to do when specific key is pressed
                        speed_x = 5
                        speed_y = 0
                    elif event.key == pygame.K_LEFT:
                        speed_x = -5
                        speed_y = 0
                    elif event.key == pygame.K_UP:
                        speed_y = -5
                        speed_x = 0
                    elif event.key == pygame.K_DOWN:
                        speed_y = 5
                        speed_x = 0


            snake_x = snake_x + speed_x
            snake_y = snake_y + speed_y

            # snake eats food
            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score +=10
                snake_size += 4
                food_x = random.randint(5, 800)
                food_y = random.randint(5, 600)

            if snake_x == 0 or snake_y == 0 or snake_x == 800 or snake_y == 600:
                game_over = True

            if [snake_x,snake_y] in snake_list[:-1]:
                game_over = True

            game.fill(white)   # color again to hide previous dot
            show_score(f'Score: {score}',blue,6,6)
            if score > int(highest):
                show_score(f'Highest Score {score}', (100, 100, 0), 6, 40)
            else:
                show_score(f'Highest Score {highest}',(100,100,0),6,40)
            draw_snake(black,snake_list) # draw snake
            pygame.draw.circle(game, red, [food_x, food_y], 6)  # creating food

            if score > int(highest):
                broken = True
                myfile = open('snk hi scr.txt', 'w')
                myfile.write(str(score))
                myfile.close()
            clock.tick(75)
            pygame.display.update() # update after changing anything in display

gameplay()
