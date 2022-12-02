import pygame
from logintest import *
import globalVariable as gv
#from quiz import *
from pyquiz5 import *

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill('deepskyblue4')
pygame.display.update()
font = pygame.font.SysFont('Arial', 25)
userpassfont = pygame.font.SysFont('Arial', 15)
Scores = []
#from src.InputBox.py import InputBox


def homescreen2():
    infinite = True
    color = "deepskyblue4"
    gv.appState = "homeScreen"
    while infinite == True:
        while gv.appState == "homeScreen":
            screen.fill(color)
            homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
            exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
            loginButt = pygame.draw.rect(screen, 'green', [10, 60, 140, 165])
            dataButt = pygame.draw.rect(screen, 'blue', [160, 60, 140, 165])
            quizButt = pygame.draw.rect(screen, 'red', [310, 60, 140, 165])
            resourcesButt = pygame.draw.rect(screen, 'purple',
                                             [10, 235, 140, 185])
            feedbackButt = pygame.draw.rect(screen, 'orange',
                                            [160, 235, 140, 185])
            settingsButt = pygame.draw.rect(screen, 'grey',
                                            [310, 235, 140, 185])
            screen.blit(font.render('Login', True, (0, 0, 0)), (45, 90))
            screen.blit(font.render('Data', True, (0, 0, 0)), (200, 90))
            screen.blit(font.render('Quiz', True, (0, 0, 0)), (350, 90))
            screen.blit(font.render('Resources', True, (0, 0, 0)), (17, 285))
            screen.blit(font.render('Feedback', True, (0, 0, 0)), (170, 285))
            screen.blit(font.render('Settings', True, (0, 0, 0)), (330, 285))
            screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
            screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homeButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()
                    if loginButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "loginScreen"
                    if dataButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "dataScreen"
                    if quizButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "quizScreen"
                    if resourcesButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "resourceScreen"
                    if feedbackButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "feedbackScreen"
                    if settingsButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "settingsScreen"
                #appLogo = pygame.draw.rect(screen, (IMAGE), [5,5,590,40])

        while gv.appState == "loginScreen":
            screen.fill("green")
            #topscreen()
            homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
            exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
            screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
            screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
            screen.blit(userpassfont.render('Username', True, (0, 0, 0)),
                        (60, 75))
            screen.blit(userpassfont.render('Password', True, (0, 0, 0)),
                        (60, 150))
            pygame.display.flip()
            inputBoxDraw()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homeButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()

        while gv.appState == "dataScreen":
            screen.fill("blue")
            homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
            exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
            screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
            screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
            screen.blit(font.render('Scores:', True, (0, 0, 0)), (10, 65))
            Scores.append(points)
            #inputDataButton = pygame.draw.rect(screen, 'white', [40,60,520,100])
            #screen.blit(pygame.font.SysFont('Arial', 15).render(score, True, (0,0,0)), (10, 100))
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
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()

        while gv.appState == "quizScreen":
            homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
            exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
            screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
            screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
            screen.fill("red")
            loop()
            
            # choice1 = pygame.draw.rect(screen, 'white', [120,70,250,40])
            # choice2 = pygame.draw.rect(screen, 'white', [120,120,250,40])
            # choice3 = pygame.draw.rect(screen, 'white', [120,170,250,40])
            # choice4 = pygame.draw.rect(screen, 'white', [120,220,250,40])
            # nextButt = pygame.draw.rect(screen, 'white', [210,270,75,30])

            # question = ""

            # screen.blit(font.render('A. Q1ChoiceA...', True, (0,0,0)), (120, 70))
            # screen.blit(font.render('B. Q1ChoiceB...', True, (0,0,0)), (120, 120))
            # screen.blit(font.render('C. Q1ChoiceC', True, (0,0,0)), (120, 170))
            # screen.blit(font.render('D. Q1ChoiceD', True, (0,0,0)), (120, 220))
            # screen.blit(font.render('Next', True, (0,0,0)), (215, 270))
            # screen.blit(font.render(question, True, ('white')), (215, 75))

            # pygame.display.update()
            # #quiz.quizsetup()
            # questionCounter = 0
            # quizScore = 0
            # for event in pygame.event.get():

            #   if questionCounter == 1:
            #   screen.blit(font.render(question, True, ('black')), (215, 75))
            #   question = "q2"
            #   screen.blit(font.render(question, True, ('white')), (215, 75))
            #   screen.blit(font.render('A. Q1ChoiceA...', True, ('white')), (120, 70))
            #   screen.blit(font.render('B. Q1ChoiceB...', True, ('white')), (120, 120))
            #   screen.blit(font.render('C. Q1ChoiceC', True, ('white')), (120, 170))
            #   screen.blit(font.render('D. Q1ChoiceD', True, ('white')), (120, 220))
            #   screen.blit(font.render('A. Q2ChoiceA...', True, (0,0,0)), (120, 70))
            #   screen.blit(font.render('B. Q2ChoiceB...', True, (0,0,0)), (120, 120))
            #   screen.blit(font.render('C. Q2ChoiceC', True, (0,0,0)), (120, 170))
            #   screen.blit(font.render('D. Q2ChoiceD', True, (0,0,0)), (120, 220))
            #   pygame.display.update()
            # if questionCounter == 2:
            #   screen.blit(font.render(question, True, ('black')), (215, 75))
            #   question = "q3"
            #   screen.blit(font.render(question, True, ('white')), (215, 75))
            #   pygame.display.update()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if choice1.collidepoint(pygame.mouse.get_pos()):
            #       quizScore = quizScore + 1
            #       print(quizScore)
            #     if choice2.collidepoint(pygame.mouse.get_pos()):
            #       quizScore = quizScore + 2
            #       print(quizScore)
            #     if choice3.collidepoint(pygame.mouse.get_pos()):
            #       quizScore = quizScore + 3
            #       print(quizScore)
            #     if choice4.collidepoint(pygame.mouse.get_pos()):
            #       quizScore = quizScore + 4
            #       print(quizScore)
            #     if nextButt.collidepoint(pygame.mouse.get_pos()):
            #       questionCounter = questionCounter + 1
            #       print(questionCounter)
            # if homeButt.collidepoint(pygame.mouse.get_pos()):
            #       gv.appState = "homeScreen"
            # if exitButt.collidepoint(pygame.mouse.get_pos()):
            #       exit()

        while gv.appState == "resourceScreen":
            screen.fill("purple")
            homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
            exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
            screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
            screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homeButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()

            screen.blit(font.render('Resources', True, (0, 0, 0)), (10, 65))

            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'Call 911 if you or someone else is in immediate danger',
                    True, (0, 0, 0)), (10, 100))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    '988 Suicide & Crisis Lifeline: Call or text 988', True,
                    (0, 0, 0)), (10, 120))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'Disaster Distress Helpline: Call or text 1-800-985-5990',
                    True, (0, 0, 0)), (10, 140))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'National Domestic Violence Hotline: 1-800-799-7233 or text LOVEIS to 22522',
                    True, (0, 0, 0)), (10, 160))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'National Sexual Assault Hotline: 1-800-656-HOPE (4673)',
                    True, (0, 0, 0)), (10, 180))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'Alzheimer’s Association Helpline: 1-800-272-3900', True,
                    (0, 0, 0)), (10, 200))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'Veteran’s Crisis Line: 988, then select 1, or Crisis Chat or text: 838255',
                    True, (0, 0, 0)), (10, 220))
            screen.blit(
                pygame.font.SysFont('Arial',
                                    20).render('Finding Treatment', True,
                                               (0, 0, 0)), (10, 250))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'FindTreatment.gov: Find a provider', True, (0, 0, 0)),
                (10, 280))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'American Psychiatric Association Foundation: Find a Psychiatrist',
                    True, (0, 0, 0)), (10, 300))
            screen.blit(
                pygame.font.SysFont('Arial', 15).render(
                    'American Psychological Association: Find a Psychologist',
                    True, (0, 0, 0)), (10, 320))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homeButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()

        while gv.appState == "feedbackScreen":
            screen.fill("orange")
            homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
            exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
            screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
            screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homeButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()

        while gv.appState == "settingsScreen":
            clickedYes = False
            clickedNo = False
            flag = True
            while flag:
                screen.fill(color)
                homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
                exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
                screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
                screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
                
                if (clickedYes):
                  aquaButt = pygame.draw.rect(screen, 'aqua', [5, 190, 60, 60])
                  magentaButt = pygame.draw.rect(screen, 'magenta', [100, 190, 60, 60])
                  maroonButt = pygame.draw.rect(screen, 'maroon', [200, 190, 60, 60])
                  screen.blit(
                                pygame.font.SysFont('Arial', 20).render(
                                    'What color?', True, (0, 0, 0)), (10, 160))
                else:
                  aquaButt = pygame.draw.rect(screen, color, [5, 190, 60, 60])
                  magentaButt = pygame.draw.rect(screen, color, [100, 190, 60, 60])
                  maroonButt = pygame.draw.rect(screen, color, [200, 190, 60, 60])
                  
                if (clickedNo):
                  screen.blit(
                                pygame.font.SysFont('Arial', 20).render(
                                    'Okay!', True, (0, 0, 0)), (10, 160))

                if (not clickedYes and not clickedNo):  
                  yesButt = pygame.draw.rect(screen, 'white', [5, 85, 60, 60])
                  noButt = pygame.draw.rect(screen, 'white', [100, 85, 60, 60])
                  screen.blit(
                      pygame.font.SysFont('Arial',
                                          20).render('Yes', True, (0, 0, 0)),
                      (5, 85))
                  screen.blit(
                      pygame.font.SysFont('Arial', 20).render('No', True, (0, 0, 0)),
                      (100, 85))
                  screen.blit(
                      pygame.font.SysFont('Arial',
                                          20).render('Change background color?',
                                                     True, (0, 0, 0)), (10, 65))
                else:
                  yesButt = pygame.draw.rect(screen, color, [5, 85, 60, 60])
                  noButt = pygame.draw.rect(screen, color, [100, 85, 60, 60])
                  
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exitButt.collidepoint(pygame.mouse.get_pos()):
                            exit()
                        if homeButt.collidepoint(pygame.mouse.get_pos()):
                            gv.appState = "homeScreen"
                            flag = False
                            break
                        if yesButt.collidepoint(pygame.mouse.get_pos()):
                            clickedYes = True
                        if aquaButt.collidepoint(pygame.mouse.get_pos()):
                            color = 'aqua'
                        if magentaButt.collidepoint(pygame.mouse.get_pos()):
                            color = 'magenta'
                        if maroonButt.collidepoint(pygame.mouse.get_pos()):
                            color = 'maroon'

                        if noButt.collidepoint(pygame.mouse.get_pos()):
                            clickedNo = True


homescreen2()
