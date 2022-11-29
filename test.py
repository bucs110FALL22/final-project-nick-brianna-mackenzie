import pygame


pygame.init()
screen = pygame.display.set_mode((600,400))
#size = pygame.display.get_window_size()

screen.fill("black")

font = pygame.font.SysFont('Arial', 25)

# pygame.draw.rect(screen, 'green', [200,150,50,50])

screen.fill('red', rect=[200,200,50,50])

loginButt = pygame.draw.rect(screen, 'green', [10,10,140,185])
dataButt = pygame.draw.rect(screen, 'blue', [160,10,140,185])
quizButt = pygame.draw.rect(screen, 'red', [310,10,140,185])
resourcesButt = pygame.draw.rect(screen, 'purple', [10,205,140,185])
feedbackButt = pygame.draw.rect(screen, 'orange', [160,205,140,185])
settingsButt = pygame.draw.rect(screen, 'grey', [310,205,140,185])

screen.blit(font.render('Login', True, (0,0,0)), (45, 90)) #login
screen.blit(font.render('Data', True, (0,0,0)), (20, 90)) #data
screen.blit(font.render('Quiz', True, (0,0,0)), (350, 90)) #quiz
screen.blit(font.render('Resources', True, (0,0,0)), (17, 285)) #resources
screen.blit(font.render('Feedback', True, (0,0,0)), (170, 285)) #feedback
screen.blit(font.render('Settings', True, (0,0,0)), (330, 285)) #settings

pygame.display.update()

input("Enter to exit")