from random import randint
from shutil import move
from tkinter import YView
from turtle import width
import pygame
import random

FPS = 60

WIDTH,HEIGHT = 800, 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
BRICK_WIDTH = 50
BRICK_HEIGHT = 16

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption ("Brick Breaker")

# Class for creating the paddle object that takes in an x and y location in addition to the width, height and color of the rectangular paddle
class Paddle:
    VEL = 10
    def __init__(self,x,y,width,height,color) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    # Method to draw the paddle object
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    # Method to change the position of the paddle object
    def move (self,direction =1):
        self.x = self.x + self.VEL *direction

class Ball:
    VEL = 5

    def __init__(self,x,y,radius,color):
         self.x = x
         self.y = y
         self.radius = radius
         self.color = color
         self.x_vel = 0
         self.y_vel = -self.VEL
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

    def move(self):
        self.x+= self.x_vel
        self.y+= self.y_vel
    
    def set_vel(self, x_vel,y_vel):
        self.x_vel= x_vel
        self.y_vel= y_vel
class Brick:
    def __init__(self, x, y , width, height, color):
        self.x = x
        self. y = y
        self.width =width
        self.height = height
        self.color = color
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    #def breakBrick(self,win):

def draw(win,paddle,ball,brick1,brick2):
    win.fill("white")
    paddle.draw(win)
    ball.draw(win)
    brick1.draw(win)
    brick2.draw(win)
    pygame.display.update()

def ball_collision(ball,paddle):
    if ball.x - BALL_RADIUS <= 0 or ball.x+BALL_RADIUS >= WIDTH:
        ball.set_vel(ball.x_vel *-1 , ball.y_vel)
    if ball.y+ BALL_RADIUS >= HEIGHT or ball.y- BALL_RADIUS <= 0:
        ball.set_vel(ball.x_vel  , ball.y_vel*-1)
    
    #working logic for hitting center paddle
    if ball.x == paddle.x+PADDLE_WIDTH/2 and ball.y-BALL_RADIUS >= paddle.y - PADDLE_HEIGHT:
        ball.set_vel(ball.x_vel , ball.y_vel*-1)
    # case for hitting left half 
    if ball.x >= paddle.x and ball.x < paddle.x+PADDLE_WIDTH/2 and ball.y-BALL_RADIUS >= paddle.y - PADDLE_HEIGHT:
        ball.set_vel(-5, ball.y_vel*-1)
    if ball.x > paddle.x+PADDLE_WIDTH/2 and ball.x < paddle.x+PADDLE_WIDTH and ball.y-BALL_RADIUS >= paddle.y - PADDLE_HEIGHT:
        ball.set_vel(5, ball.y_vel*-1)   
def main():
    clock = pygame.time.Clock()
    paddle = Paddle(WIDTH/2-PADDLE_WIDTH/2,HEIGHT-PADDLE_HEIGHT-10,PADDLE_WIDTH,PADDLE_HEIGHT,"Red")
    ball = Ball(WIDTH/2,HEIGHT-PADDLE_HEIGHT-BALL_RADIUS-10,BALL_RADIUS,"Blue")
    #initializing brick locations at random x,y
    brick1 = Brick(random.randint(0+BRICK_WIDTH/2,WIDTH-BRICK_WIDTH/2),random.randint(0+BRICK_HEIGHT/2,HEIGHT/2-BRICK_HEIGHT/2),BRICK_WIDTH,BRICK_HEIGHT,"Black")
    brick2 = Brick(random.randint(0+BRICK_WIDTH/2,WIDTH-BRICK_WIDTH/2),random.randint(0+BRICK_HEIGHT/2,HEIGHT/2-BRICK_HEIGHT/2),BRICK_WIDTH,BRICK_HEIGHT,"Black")
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.x-paddle.VEL>= 0:
            paddle.move(-1)
        if keys[pygame.K_RIGHT] and paddle.x +paddle.VEL<=WIDTH-PADDLE_WIDTH:
            paddle.move()

        ball.move()
        ball_collision(ball,paddle)
        draw(win,paddle,ball,brick1,brick2)
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()