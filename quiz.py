import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode((600,400))
#screen.fill("red")
choice1 = pygame.draw.rect(screen, 'white', [120,70,250,40])
choice2 = pygame.draw.rect(screen, 'white', [120,120,250,40])
choice3 = pygame.draw.rect(screen, 'white', [120,170,250,40])
choice4 = pygame.draw.rect(screen, 'white', [120,220,250,40])
nextButt = pygame.draw.rect(screen, 'white', [210,270,75,30])

homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
def Q3():
  screen.blit(font.render('A. Q3ChoiceA...', True, (0,0,0)), (120, 70))
  screen.blit(font.render('B. Q3ChoiceB...', True, (0,0,0)), (120, 120))
  screen.blit(font.render('C. Q3ChoiceC', True, (0,0,0)), (120, 170))
  screen.blit(font.render('D. Q3ChoiceD', True, (0,0,0)), (120, 220))
  screen.blit(font.render('Next3', True, (0,0,0)), (215, 270))
def Q2():
  screen.blit(font.render('A. Q2ChoiceA...', True, (0,0,0)), (120, 70))
  screen.blit(font.render('B. Q2ChoiceB...', True, (0,0,0)), (120, 120))
  screen.blit(font.render('C. Q2ChoiceC', True, (0,0,0)), (120, 170))
  screen.blit(font.render('D. Q2ChoiceD', True, (0,0,0)), (120, 220))
def quizsetup():
  infinite = True
  
  appState = "quizScreen"
  while infinite == True:
    while appState == "quizScreen":
      #choice1
      #choice2
      #choice3
      #choice4
      #homeButt
      #exitButt
      screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
      screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
      pygame.display.update()
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if nextButt.collidepoint(pygame.mouse.get_pos()):
                  appState = "quizScreen"
                  print('next')
                  screen.blit(font.render('A. Q1ChoiceA...', True, ('white')), (120, 70))
                  screen.blit(font.render('B. Q1ChoiceB...', True, ('white')), (120, 120))
                  screen.blit(font.render('C. Q1ChoiceC', True, ('white')), (120, 170))
                  screen.blit(font.render('D. Q1ChoiceD', True, ('white')), (120, 220))
                  screen.blit(font.render('Next', True, ('white')), (215, 270))
                  Q2()
                  next2Butt = pygame.draw.rect(screen, 'white', [210,270,75,30])
          if event.type == pygame.MOUSEBUTTONDOWN:
            if next2Butt.collidepoint(pygame.mouse.get_pos()):
                  appState = "quizScreen"
                  print('next2')

                  screen.blit(font.render('A. Q2ChoiceA...', True, ('white')), (120, 70))
                  screen.blit(font.render('B. Q2ChoiceB...', True, ('white')), (120, 120))
                  screen.blit(font.render('C. Q2ChoiceC', True, ('white')), (120, 170))
                  screen.blit(font.render('D. Q2ChoiceD', True, ('white')), (120, 220))
                  screen.blit(font.render('Next2', True, ('white')), (215, 270))
                  Q3() 
            else:
              Q2()
      pygame.display.flip()
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
                  print('slay')
            if exitButt.collidepoint(pygame.mouse.get_pos()):
                  exit()

screen.blit(font.render('A. Q1ChoiceA...', True, (0,0,0)), (120, 70))
screen.blit(font.render('B. Q1ChoiceB...', True, (0,0,0)), (120, 120))
screen.blit(font.render('C. Q1ChoiceC', True, (0,0,0)), (120, 170))
screen.blit(font.render('D. Q1ChoiceD', True, (0,0,0)), (120, 220))
screen.blit(font.render('Next', True, (0,0,0)), (215, 270))
pygame.display.update()
quizsetup()


  # for event in pygame.event.get():
  #   if event.type == pygame.MOUSEBUTTONDOWN:
  #     if nextButt.collidepoint(pygame.mouse.get_pos()):
  #       quizsetup()
      
if __name__ == '__main__':
  quizsetup()
  pygame.quit()



