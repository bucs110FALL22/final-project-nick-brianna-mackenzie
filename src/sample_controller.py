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
    self.font = pygame.font.SysFont('Arial', 25)

  # def homeAndExit(self):
  #   self.homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
  #   self.exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
  #   self.screen.blit(self.font.render('Home', True, (0,0,0)), (200, 10))
  #   self.screen.blit(self.font.render('Exit', True, (0,0,0)), (400, 10))
    
  def mainloop(self):
    #select state loop
    infinite = True
    appState = "homeScreen"
    while infinite == True:
      while appState == "homeScreen":
        self.screen.fill("deepskyblue4")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        loginButt = pygame.draw.rect(self.screen, 'green', [10,60,140,165])
        dataButt = pygame.draw.rect(self.screen, 'blue', [160,60,140,165])
        quizButt = pygame.draw.rect(self.screen, 'red', [310,60,140,165])
        resourcesButt = pygame.draw.rect(self.screen, 'purple', [10,235,140,185])
        feedbackButt = pygame.draw.rect(self.screen, 'orange', [160,235,140,185])
        settingsButt = pygame.draw.rect(self.screen, 'grey', [310,235,140,185])
        self.screen.blit(font.render('Login', True, (0,0,0)), (45, 90))
        self.screen.blit(font.render('Data', True, (0,0,0)), (200, 90))
        self.screen.blit(font.render('Quiz', True, (0,0,0)), (350, 90))
        self.screen.blit(font.render('Resources', True, (0,0,0)), (17, 285))
        self.screen.blit(font.render('Feedback', True, (0,0,0)), (170, 285))
        self.screen.blit(font.render('Settings', True, (0,0,0)), (330, 285))
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
            if loginButt.collidepoint(pygame.mouse.get_pos()):
              appState = "loginScreen"
            if dataButt.collidepoint(pygame.mouse.get_pos()):
              appState = "dataScreen"
            if quizButt.collidepoint(pygame.mouse.get_pos()):
              appState = "quizScreen"
            if resourcesButt.collidepoint(pygame.mouse.get_pos()):
              appState = "resourceScreen"
            if feedbackButt.collidepoint(pygame.mouse.get_pos()):
              appState = "feedbackScreen"
            if settingsButt.collidepoint(pygame.mouse.get_pos()):
              appState = "settingsScreen"
            #appLogo = pygame.draw.rect(screen, (IMAGE), [5,5,590,40])
      
      while appState == "loginScreen":
        self.screen.fill("green")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
      
      while appState == "dataScreen":
        self.screen.fill("blue")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
      
      while appState == "quizScreen":
        self.screen.fill("red")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
          
      while appState == "resourceScreen":
        self.screen.fill("purple")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
      
      while appState == "feedbackScreen":
        self.screen.fill("orange")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
            
      while appState == "settingsScreen":
        self.screen.fill("grey")
        homeButt = pygame.draw.rect(self.screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(self.screen, 'white', [400,0,50,50])
        self.screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        self.screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
      
  
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
