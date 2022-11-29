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
            if # CHECK FOR COLLISION WITH BUTTONS + REPEAT
              #code to enter new screen based on what was pressed and exit loop to new menu
      pygame.draw.rect(self.screen, (IMAGE), [x,y,w,h]) #app logo on top
    
      pygame.draw.rect(self.screen, 'green', [x,y,w,h]) #login button
      pygame.draw.rect(self.screen, 'blue', [x,y,w,h]) #data button
      pygame.draw.rect(self.screen, 'red', [x,y,w,h]) #quiz button
      pygame.draw.rect(self.screen, 'purple', [x,y,w,h]) #resour button
      pygame.draw.rect(self.screen, 'orange', [x,y,w,h]) #feed button
      pygame.draw.rect(self.screen, 'grey', [x,y,w,h]) #settings button?
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
