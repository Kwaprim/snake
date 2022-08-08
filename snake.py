from cgitb import text
import pygame as p
from pygame.locals import *
import time
import random as r

class Game:
    def __init__(self):
        p.init()
        # setting screensize
        self.screen = p.display.set_mode((960,800)) 
        
        # changing the title to Snake
        self.title = p.display.set_caption("Snake")
        
        # adding background color
        self.screen_color = self.screen.fill((0, 128, 0))
        
        # adding the snake logo
        self.icon = p.image.load('snake.png').convert()
        p.display.set_icon(self.icon)
        
        # drawing snake head
        self.snake_head = p.image.load('square.png').convert() 
        self.snake_length = 1
        self.snake_head_x = [32] * self.snake_length
        self.snake_head_y = [32] * self.snake_length
        self.screen.blit(self.snake_head,(self.snake_head_x[0],self.snake_head_y[0]))
        
        p.display.update()
        
    def motion_draw(self):
        """This function when called will fill the screen with the background and draw the snake head to make player perceive the snake head moving"""
        
        self.screen_color = self.screen.fill((0, 128, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.snake_head, (self.snake_head_x[i], self.snake_head_y[i]))
            
        p.display.update()
        
    def Food(self):
        self.food = p.image.load('food.png').convert()
        self.food_x = 320
        self.food_y = 320
        self.screen.blit(self.food, (self.food_x, self.food_x))
        
        
        p.display.update()
        
    def Score(self):
        if abs(self.food_y - self.snake_head_y[0]) < 32 or abs(self.food_x - self.snake_head_x[0]) < 32:
            self.snake_length += 1
            self.snake_head_x.append(-1)
            self.snake_head_y.append(-1)
            self.food_x = r.randint(1,30)
            self.food_y = r.randint(1,25)
            self.screen.blit(self.food, (self.food_x, self.food_x))
            
        t_score = p.font.SysFont('georgia',30)
        score = t_score.render(f"Score: {self.snake_length}",True,(255,255,255))
        self.screen.blit(score,(800,10))
        
        
    def Gameover(self):
        pass  
    
    
    def playing(self):
        running = True
        
        while running:
            for event in p.event.get():
                if event.type() == QUIT: # Game quit when player clicks close 
                    running = False
                if event.type() == KEYDOWN:
                    if event.key() == K_ESCAPE: # Setting ESC as an alternate close key
                        running = False
                    # movement description for snake head 
                    if event.key == K_LEFT:
                        self.snake_head_x -= 32
                    
                    if event.key == K_RIGHT:
                        self.snake_head_x += 32

                    if event.key == K_UP:
                        self.snake_head_y -= 32

                    if event.key == K_DOWN:
                        self.snake_head_y += 32
            
            for i in range(self.length - 1, 0, -1):
                self.snake_head_x[i] = self.snake_head_x[i - 1]
                self.snake_head_y[i] = self.snake_head_y[i - 1]
            
            
            self.motion_draw()
            
            time.sleep(.2) # snake head move in a maintained direction every .2 secs
    




if __name__ == "__main__":
    game = Game()
    game.playing()
    





    
    
