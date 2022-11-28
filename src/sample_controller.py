import pygame
from src.Rectangle.py import Rectangle
from src.Surface.py import Surface

class Controller:
  
  def __init__(self):
    #setup pygame data

    pygame.init()
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()
    self.background = "deepskyblue3"
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
