import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 500

black = pygame.Color(1, 1, 43)
blue = pygame.Color(5, 217, 232)
navy = pygame.Color(0, 86, 120)
red = pygame.Color(255, 42, 109)
white = pygame.Color(209, 247, 255)

pygame.init()

pygame.display.set_caption('snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

wall = [[x, 240] for x in range(180, 540, 20)]

snake_position = [100, 60]

snake_body = [[100, 60],
              [80, 60],
              [60, 60],
              [40, 60]]

apple_position = [random.randrange(1, (window_x//20)) * 20,
				random.randrange(1, (window_y//20)) * 20]

apple_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('score: ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

def game_over():    
    for index, pos in enumerate(snake_body):
        if index == 1:
            pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 20, 20))
            pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 20, 20), 2) 

            if direction == 'UP':
                pygame.draw.line(game_window, red, (pos[0]+5, pos[1]+7), (pos[0]+7, pos[1]+9), 1)
                pygame.draw.line(game_window, red, (pos[0]+7, pos[1]+7), (pos[0]+5, pos[1]+9), 1)

                pygame.draw.line(game_window, red, (pos[0]+12, pos[1]+7), (pos[0]+14, pos[1]+9), 1)
                pygame.draw.line(game_window, red, (pos[0]+14, pos[1]+7), (pos[0]+12, pos[1]+9), 1)
            elif direction == 'DOWN':
                pygame.draw.line(game_window, red, (pos[0]+5, pos[1]+12), (pos[0]+7, pos[1]+14), 1)
                pygame.draw.line(game_window, red, (pos[0]+7, pos[1]+12), (pos[0]+5, pos[1]+14), 1)

                pygame.draw.line(game_window, red, (pos[0]+12, pos[1]+12), (pos[0]+14, pos[1]+14), 1)
                pygame.draw.line(game_window, red, (pos[0]+14, pos[1]+12), (pos[0]+12, pos[1]+14), 1)
            elif direction == 'LEFT':
                pygame.draw.line(game_window, red, (pos[0]+7, pos[1]+5), (pos[0]+9, pos[1]+7), 1)
                pygame.draw.line(game_window, red, (pos[0]+9, pos[1]+5), (pos[0]+7, pos[1]+7), 1)

                pygame.draw.line(game_window, red, (pos[0]+7, pos[1]+12), (pos[0]+9, pos[1]+14), 1)
                pygame.draw.line(game_window, red, (pos[0]+9, pos[1]+12), (pos[0]+7, pos[1]+14), 1)
            elif direction == 'RIGHT':
                pygame.draw.line(game_window, red, (pos[0]+12, pos[1]+5), (pos[0]+14, pos[1]+7), 1)
                pygame.draw.line(game_window, red, (pos[0]+14, pos[1]+5), (pos[0]+12, pos[1]+7), 1)

                pygame.draw.line(game_window, red, (pos[0]+12, pos[1]+12), (pos[0]+14, pos[1]+14), 1)
                pygame.draw.line(game_window, red, (pos[0]+14, pos[1]+12), (pos[0]+12, pos[1]+14), 1)
       
    pygame.display.update()
    time.sleep(1)

    my_font = pygame.font.SysFont('microsoftjhenghei', 50)
    game_over_surface = my_font.render('your score is: ' + str(score), True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                time.sleep(2)
                pygame.quit()
                quit()
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snake_position[1] -= 20
    if direction == 'DOWN':
        snake_position[1] += 20
    if direction == 'LEFT':
        snake_position[0] -= 20
    if direction == 'RIGHT':
        snake_position[0] += 20
        
    snake_body.insert(0, list(snake_position))
    
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    for block in wall:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    if (abs(snake_position[0] - apple_position[0]) < 20) and (abs(snake_position[1] - apple_position[1]) < 20):
        score += 1
        apple_spawn = False
    else:
        snake_body.pop()
        
    if not apple_spawn:
        while True:
            apple_x_options = list(range(20, 160, 20)) + list(range(560, window_x - 20, 20))
            apple_position_x = random.choice(apple_x_options)
                
            apple_y_options = list(range(20, 220, 20)) + list(range(260, window_y - 20, 20))
            apple_position_y = random.choice(apple_y_options)

            apple_position = [apple_position_x, apple_position_y]
            
            if any(ap == wp for wp in wall for ap in apple_position) or any(ap == sb for sb in snake_body for ap in apple_position):
                continue
            else:
                break

    apple_spawn = True

    for x in range(0, window_x, 20):
        for y in range(0, window_y, 20):
            pygame.draw.rect(game_window, navy if (x // 20) % 2 == (y // 20) % 2 else black, pygame.Rect(x, y, 20, 20))
    
    for pos in wall:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 20, 20))

    for index, pos in enumerate(snake_body):
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 20, 20))
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 20, 20), 2) 

        if index == 0:  
            if direction == 'UP':
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 5, pos[1] + 7, 3, 3))  
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 12, pos[1] + 7, 3, 3)) 
                pygame.draw.rect(game_window, red, pygame.Rect(pos[0] + 9, pos[1] - 5, 2, 5)) 
            elif direction == 'DOWN':
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 5, pos[1] + 12, 3, 3))  
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 12, pos[1] + 12, 3, 3)) 
                pygame.draw.rect(game_window, red, pygame.Rect(pos[0] + 9, pos[1] + 20, 2, 5)) 
            elif direction == 'LEFT':
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 5, pos[1] + 5, 3, 3))  
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 5, pos[1] + 12, 3, 3)) 
                pygame.draw.rect(game_window, red, pygame.Rect(pos[0] - 5, pos[1] + 9, 5, 2)) 
            elif direction == 'RIGHT':
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 12, pos[1] + 5, 3, 3))  
                pygame.draw.rect(game_window, black, pygame.Rect(pos[0] + 12, pos[1] + 12, 3, 3)) 
                pygame.draw.rect(game_window, red, pygame.Rect(pos[0] + 20, pos[1] + 9, 5, 2))

    pygame.draw.circle(game_window, red, [apple_position[0] + 10, apple_position[1] + 10], 10)
    pygame.draw.rect(game_window, black, pygame.Rect(apple_position[0] + 9, apple_position[1], 2, 5))
            
    show_score(1, white, 'microsoftjhenghei', 30)
    
    pygame.display.update()
    
    fps.tick(snake_speed)