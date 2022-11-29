import pygame


pygame.init()
screen = pygame.display.set_mode((400,300))
#size = pygame.display.get_window_size()

screen.fill("blue")

# pygame.draw.rect(screen, 'green', [200,150,50,50])

screen.fill('red', rect=[200,200,50,50])

pygame.display.update()

input("Enter to exit")