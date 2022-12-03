import pygame
#from src.InputBox.py import InputBox

pygame.init()
screen = pygame.display.set_mode((600,400))
screen.fill("deepskyblue4")
pygame.display.update()
font = pygame.font.SysFont('Arial', 25)

infinite = True

appState = "homeScreen"
while infinite == True:
  while appState == "homeScreen":
    screen.fill("deepskyblue4")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    loginButt = pygame.draw.rect(screen, 'green', [10,60,140,165])
    dataButt = pygame.draw.rect(screen, 'blue', [160,60,140,165])
    quizButt = pygame.draw.rect(screen, 'red', [310,60,140,165])
    resourcesButt = pygame.draw.rect(screen, 'purple', [10,235,140,185])
    feedbackButt = pygame.draw.rect(screen, 'orange', [160,235,140,185])
    settingsButt = pygame.draw.rect(screen, 'grey', [310,235,140,185])
    screen.blit(font.render('Login', True, (0,0,0)), (45, 90))
    screen.blit(font.render('Data', True, (0,0,0)), (200, 90))
    screen.blit(font.render('Quiz', True, (0,0,0)), (350, 90))
    screen.blit(font.render('Resources', True, (0,0,0)), (17, 285))
    screen.blit(font.render('Feedback', True, (0,0,0)), (170, 285))
    screen.blit(font.render('Settings', True, (0,0,0)), (330, 285))
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
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
    screen.fill("green")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if homeButt.collidepoint(pygame.mouse.get_pos()):
                appState = "homeScreen"
          if exitButt.collidepoint(pygame.mouse.get_pos()):
                exit()
  
  while appState == "dataScreen":
    screen.fill("blue")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    inputDataButton = pygame.draw.rect(screen, 'white', [40,60,520,100])
    pygame.display.update()
    # clock = pg.time.Clock()
    # input_box1 = InputBox(50,70,140,32,text='Input x-axis')
    # input_box2 = InputBox(50,110,140,32,text='Input y-axis')
    # input_boxes = [input_box1, input_box2]
    # done = False

    # while not done:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             done = True
    #         for box in input_boxes:
    #             box.handle_event(event)

    #     for box in input_boxes:
    #         box.update()

    #     screen.fill((30, 30, 30))
    #     for box in input_boxes:
    #         box.draw(screen)

    #     pg.display.flip()
    #     clock.tick(30)
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          if homeButt.collidepoint(pygame.mouse.get_pos()):
              appState = "homeScreen"
          if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
  
  while appState == "quizScreen":
    screen.fill("red")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          if homeButt.collidepoint(pygame.mouse.get_pos()):
                appState = "homeScreen"
          if exitButt.collidepoint(pygame.mouse.get_pos()):
                exit()
      
  while appState == "resourceScreen":
    screen.fill("purple")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          if homeButt.collidepoint(pygame.mouse.get_pos()):
                appState = "homeScreen"
          if exitButt.collidepoint(pygame.mouse.get_pos()):
                exit()
  
  while appState == "feedbackScreen":
    screen.fill("orange")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          if homeButt.collidepoint(pygame.mouse.get_pos()):
                appState = "homeScreen"
          if exitButt.collidepoint(pygame.mouse.get_pos()):
                exit()
        
  while appState == "settingsScreen":
    screen.fill("grey")
    homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          if homeButt.collidepoint(pygame.mouse.get_pos()):
                appState = "homeScreen"
          if exitButt.collidepoint(pygame.mouse.get_pos()):
                exit()