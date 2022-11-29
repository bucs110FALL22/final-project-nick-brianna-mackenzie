import pygame
import tkinter as tk
from tkinter import ttk
from src.Rectangle.py import Rectangle
from src.Surface.py import Surface

class Controller:
  
  def __init__(self):
    #setup pygame data

    pygame.init()
    self.screen = pygame.display.set_mode((600,400))
    self.screen.fill("deepskyblue4")
    pygame.display.update()
    
  def mainloop(self):
    #select state loop
    appExit = False
    while not appExit:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          gameExit = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.MOUSE_DOWN:
            mousePos = pygame.mouse.get_pos()
            if loginButt.collidepoint(mousePos) == True:
              #enter new screen based on whats pressed
            if dataButt.collidepoint(mousePos) == True:
              #enter new screen based on whats pressed
            if quizButt.collidepoint(mousePos) == True:
              #enter new screen based on whats pressed
            if resourcesButt.collidepoint(mousePos) == True:
              #enter new screen based on whats pressed
            if feedbackButt.collidepoint(mousePos) == True:
              #enter new screen based on whats pressed
            if settingsButt.collidepoint(mousePos) == True:
              #enter new screen based on whats pressed
      appLogo = pygame.draw.rect(self.screen, (IMAGE), [x,y,w,h])
    
      loginButt = pygame.draw.rect(self.screen, 'green', [x,y,w,h])
      dataButt = pygame.draw.rect(self.screen, 'blue', [x,y,w,h])
      quizButt = pygame.draw.rect(self.screen, 'red', [x,y,w,h])
      resourcesButt = pygame.draw.rect(self.screen, 'purple', [x,y,w,h])
      feedbackButt = pygame.draw.rect(self.screen, 'orange', [x,y,w,h])
      settingsButt = pygame.draw.rect(self.screen, 'grey', [x,y,w,h])
      '''
      FILL IN COORDS TO DRAW THESE BUTTONS ^^^^^^^
      '''
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
