import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
rect1 = Rect(20,20,20,20)
rect2=rect1.copy()
running = True
x=0
y=0
while running:
   for event in pygame.event.get():
      if event.type == QUIT:
         running = False
      if event.type == KEYDOWN:
         if event.key==K_LEFT:
            x= -20
            y=0
         if event.key == K_RIGHT:
            x=20
            y=0
         if event.key == K_UP:
            x = 0
            y = -20
         if event.key == K_DOWN:
            x = 0
            y = 20
      rect2.move_ip(x,y)
      screen.fill((127,127,127))
      pygame.draw.rect(screen, (255,0,0), rect1, 1)
      pygame.draw.rect(screen, (0,0,255), rect2, 5)
      pygame.display.update()
      # pygame.quit()