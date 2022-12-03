import pygame
import json
from src.inputbox import *
import src.globalVariable as gv
#from quiz import *
from src.quiz import *
from src.jsonAPI import *


pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill('deepskyblue4')
pygame.display.set_caption('bHealth')
pygame.display.update()
font = pygame.font.SysFont('Arial', 25)
userpassfont = pygame.font.SysFont('Arial', 15)
Scores = []
#from src.InputBox.py import InputBox


def homescreen2():
    infinite = True
    bgcolor = "deepskyblue4"
    gv.appState = "homeScreen"
    while infinite == True:
        while gv.appState == "homeScreen":
            screen.fill(bgcolor)
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
            screen.blit(font.render('3', True, (0, 0, 0)), (130, 65))
            #screen.blit(font.render(gv.quizPoints, True, (0,0,0)), (100, 100))
            #screen.blit(font.render(datanumber, True, (0, 0, 0)), (10, 85))
            #inputDataButton = pygame.draw.rect(screen, 'white', [40,60,520,100])
            #screen.blit(pygame.font.SysFont('Arial', 15).render(score, True, (0,0,0)), (10, 100))
            #jsonAPI()
            pygame.display.update()
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
            quizLoop()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if homeButt.collidepoint(pygame.mouse.get_pos()):
                        gv.appState = "homeScreen"
                    if exitButt.collidepoint(pygame.mouse.get_pos()):
                        exit()

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
            screen.blit(font.render('Leave us some feedback!', True, (0, 0, 0)), (60, 60))
            inputBoxDraw2()
            #screen.blit(font.render(gv.feedbackText, True, (0,0,0)), (100, 100))
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
                screen.fill(bgcolor)
                homeButt = pygame.draw.rect(screen, 'pink', [0, 0, 400, 50])
                exitButt = pygame.draw.rect(screen, 'white', [400, 0, 50, 50])
                screen.blit(font.render('Home', True, (0, 0, 0)), (200, 10))
                screen.blit(font.render('Exit', True, (0, 0, 0)), (400, 10))
                
                if (clickedYes):
                  aquaButt = pygame.draw.rect(screen, 'aqua', [5, 190, 60, 60])
                  magentaButt = pygame.draw.rect(screen, 'magenta', [100, 190, 60, 60])
                  maroonButt = pygame.draw.rect(screen, 'maroon', [200, 190, 60, 60])
                  originalButt = pygame.draw.rect(screen, 'deepskyblue4', [300, 190, 60, 60])
                  screen.blit(pygame.font.SysFont('Arial', 20).render('What color?', True, (0, 0, 0)), (10, 160))
                else:
                  aquaButt = pygame.draw.rect(screen, bgcolor, [5, 190, 60, 60])
                  magentaButt = pygame.draw.rect(screen, bgcolor, [100, 190, 60, 60])
                  maroonButt = pygame.draw.rect(screen, bgcolor, [200, 190, 60, 60])
                  originalButt = pygame.draw.rect(screen, bgcolor, [300, 190, 60, 60])
                  
                if (clickedNo):
                  screen.blit(pygame.font.SysFont('Arial', 20).render('Okay!', True, (0, 0, 0)), (10, 160))

                if (not clickedYes and not clickedNo):  
                  yesButt = pygame.draw.rect(screen, 'white', [5, 85, 60, 60])
                  noButt = pygame.draw.rect(screen, 'white', [100, 85, 60, 60])
                  screen.blit(
                      pygame.font.SysFont('Arial',20).render('Yes', True, (0, 0, 0)),(5, 85))
                  screen.blit(
                      pygame.font.SysFont('Arial', 20).render('No', True, (0, 0, 0)),(100, 85))
                  screen.blit(
                      pygame.font.SysFont('Arial',20).render('Change background color?',True, (0, 0, 0)), (10, 65))
                else:
                  yesButt = pygame.draw.rect(screen, bgcolor, [5, 85, 30, 30])
                  noButt = pygame.draw.rect(screen, bgcolor, [100, 85, 30, 30])
                  
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
                            bgcolor = 'aqua'
                        if magentaButt.collidepoint(pygame.mouse.get_pos()):
                            bgcolor = 'magenta'
                        if maroonButt.collidepoint(pygame.mouse.get_pos()):
                            bgcolor = 'maroon'
                        if originalButt.collidepoint(pygame.mouse.get_pos()):
                            bgcolor = 'deepskyblue4'

                        if noButt.collidepoint(pygame.mouse.get_pos()):
                            clickedNo = True


homescreen2()
