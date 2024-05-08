import pygame, random
from time import time

class Snake:
    def __init__(self):
        self.start_time = 0
        self.end_time = None
        self.win = None
        self.total_time = None

    def snake_game(self):
        w = pygame.display.set_mode((500,550),flags=pygame.SHOWN)
        # w = windows
        snake = [[9,9]]
        run = True
        move = [0,0]
        fx,fy = 0,0 # fx, fy = cooridinates for the food
        score_value = 0
        pygame.time.wait(2000)
        fx,fy = random.randint(0,19),random.randint(0,19)
        while [fx,fy] in snake:
            # respawns food to prevent from spawning inside snake
            fx,fy = random.randint(0,19),random.randint(0,19)

        #Does not move
        while run:
            self.start_time = time()
            head = snake[0]
            w.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move = [-1,0]
                    if event.key == pygame.K_RIGHT:
                        move = [1,0]
                    if event.key == pygame.K_UP:
                        move = [0,-1]
                    if event.key == pygame.K_DOWN:
                        move = [0,1]
            #Sets the key to move according x, y.
            snake.insert(0,[snake[0][0]+move[0],snake[0][1]+move[1]])
            snake.pop()
            #Deletes the previous code in an array
            for l in snake:
                x = l[0]*25
                y = l[1]*25
                pygame.draw.rect(w,(222,244,255),(x,y,25,25))
            pygame.draw.rect(w,(236,255,199),(fx*25,fy*25,25,25))
            
            if [fx,fy] == snake[0]:
                fx,fy = random.randint(0,19),random.randint(0,19) # Draws the snake
                while [fx,fy] in snake:
                    # respawns food to prevent from spawning inside snake
                    fx,fy = random.randint(0,19),random.randint(0,19)
                snake.append(head)
                score_value += 1
                
            if snake[0][0]>19 or snake[0][0]<0 or snake[0][1]>19 or snake[0][1]<0:
                # ends game if snake exits window
                run = False
            if snake[0] in snake [1:]:
                # ends game if snake touches snake
                run = False
                self.win = False
            
            WHITE = (255,255,255)
            pygame.font.init()
            font = pygame.font.Font(None, 50)
            text_render = font.render(f"{score_value}", True, WHITE)
            text_rect = text_render.get_rect(center=(500 // 2, 50))
            w.blit(text_render, text_rect)

            if score_value >= 2:
                self.end_time = time()
                run = False  
                self.win = True   
                self.total_time = self.end_time - self.start_time
                return self.total_time           
                
            pygame.display.update()
            pygame.time.Clock().tick(10)
            
            #Prints the snake (one block)
        w = pygame.display.set_mode((500,550),flags=pygame.HIDDEN)            
