import pygame


pygame.init()
screen = pygame.display.set_mode((600,400))
#size = pygame.display.get_window_size()

screen.fill("black")

font = pygame.font.SysFont('Arial', 25)

# pygame.draw.rect(screen, 'green', [200,150,50,50])

screen.fill('red', rect=[200,200,50,50])
homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
loginButt = pygame.draw.rect(screen, 'green', [10,60,140,165])
dataButt = pygame.draw.rect(screen, 'blue', [160,60,140,165])
quizButt = pygame.draw.rect(screen, 'red', [310,60,140,165])
resourcesButt = pygame.draw.rect(screen, 'purple', [10,235,140,185])
feedbackButt = pygame.draw.rect(screen, 'orange', [160,235,140,185])
settingsButt = pygame.draw.rect(screen, 'grey', [310,235,140,185])


screen.blit(font.render('Login', True, (0,0,0)), (45, 90)) #login
screen.blit(font.render('Data', True, (0,0,0)), (200, 90)) #data
screen.blit(font.render('Quiz', True, (0,0,0)), (350, 90)) #quiz
screen.blit(font.render('Resources', True, (0,0,0)), (17, 285)) #resources
screen.blit(font.render('Feedback', True, (0,0,0)), (170, 285)) #feedback
screen.blit(font.render('Settings', True, (0,0,0)), (330, 285)) #settings
screen.blit(font.render('Home', True, (0,0,0)), (200, 10)) #home
screen.blit(font.render('Exit', True, (0,0,0)), (400, 10)) #exit
pygame.display.update()
def topScreen():
  pygame.draw.rect(screen, 'white', [400,0,50,50])
  screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
  pygame.draw.rect(screen, 'pink', [0,0,400,50])
  screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
while True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:           
        if loginButt.collidepoint(pygame.mouse.get_pos()):
          print("Mouse clicked on the login button")
          screen.fill("yellow")
          topScreen()
          pygame.display.update()
        elif dataButt.collidepoint(pygame.mouse.get_pos()):
          print("Mouse clicked on the data button")
          screen.fill("purple")
          topScreen()
          pygame.display.update() 
        elif quizButt.collidepoint(pygame.mouse.get_pos()):
          print("Mouse clicked on the quiz button")
          screen.fill("red")
          topScreen()
          pygame.display.update()
        elif resourcesButt.collidepoint(pygame.mouse.get_pos()):
          print("Mouse clicked on the resources button")
          screen.fill("blue")
          topScreen()
          pygame.display.update()
        elif feedbackButt.collidepoint(pygame.mouse.get_pos()):
          print("Mouse clicked on the feedback button")
          screen.fill("green")
          topScreen()
          pygame.display.update()
        elif settingsButt.collidepoint(pygame.mouse.get_pos()):
          print("Mouse clicked on the settings button")
          screen.fill("blue")
          topScreen()
          pygame.display.update()
        elif exitButt.collidepoint(pygame.mouse.get_pos()):
         print("Mouse clicked on the exit button")
         exit()
        elif homeButt.collidepoint(pygame.mouse.get_pos()):
           print("Mouse clicked on the home button")
           screen.fill('red', rect=[200,200,50,50])
           homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
           exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
           loginButt = pygame.draw.rect(screen, 'green', [10,60,140,165])
           dataButt = pygame.draw.rect(screen, 'blue', [160,60,140,165])
           quizButt = pygame.draw.rect(screen, 'red', [310,60,140,165])
           resourcesButt = pygame.draw.rect(screen, 'purple', [10,235,140,185])
           feedbackButt = pygame.draw.rect(screen, 'orange', [160,235,140,185])
           settingsButt = pygame.draw.rect(screen, 'grey', [310,235,140,185])
                      
                      
           screen.blit(font.render('Login', True, (0,0,0)), (45, 90)) #login
           screen.blit(font.render('Data', True, (0,0,0)), (200, 90)) #data
           screen.blit(font.render('Quiz', True, (0,0,0)), (350, 90)) #quiz
           screen.blit(font.render('Resources', True, (0,0,0)), (17, 285)) #resources
           screen.blit(font.render('Feedback', True, (0,0,0)), (170, 285)) #feedback
           screen.blit(font.render('Settings', True, (0,0,0)), (330, 285)) #settings
           screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
           screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
           pygame.display.update()
