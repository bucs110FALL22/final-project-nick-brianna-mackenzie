import pygame
import pygame.gfxdraw
import sys
import time
import random
# the Label class is this module below
from label import *
import globalVariable as gv

font = pygame.font.SysFont('Arial', 25)


pygame.init()
pygame.mixer.init()
#hit = pygame.mixer.Sound("sounds/hit.wav")
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()

class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size,
        colors="white",
        hover_colors="green",
        style="button1",
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):
        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num
        self.text = text
        self.command = command
        self.colors = colors
        self.original_colors = colors
        self.fg = "black"
        self.bg = "white"
        if hover_colors == "green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc 
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def render(self, text):
        self.text_render = self.font.render(text, 1, self.fg)
        self.image = self.text_render
        
    def update(self):
        #self.fg, self.bg = self.colors.split(" on ")
        self.fg = "black"
        self.bg = "white"

        if self.style == "button1":
            self.draw_button1()
        elif self.style == "button2":
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        lcolor = ('white')
        lcolor2 = ('red')
        pygame.draw.line(screen, lcolor, self.position,
            (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, lcolor, (self.x, self.y - 2),
            (self.x, self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x, self.y + self.h),
            (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x + self.w , self.y + self.h),
            [self.x + self.w , self.y], 5)
        pygame.draw.rect(screen, self.bg, self.rect)  

    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x - 50, self.y, 500 , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colors = self.hover_colors
        else:
            self.colors = self.original_colors

    def hover(self):
        self.check_collision()

    def click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0

            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1

def on_click():
    print("Click on one answer")

def on_right():
    check_score("right")

def on_false():
    ''' if there is no 'right' as arg it means it's false '''
    check_score()

def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnum, points
    if qnum < len(questions):
        print(qnum, len(questions))
        if answered == "right":
            time.sleep(.1) 
            points += 1
           
        qnum += 1 #
        score.change_text(str(points))
       
        title.change_text(questions[qnum-1][0], color="white")
        num_question.change_text(str(qnum))
        show_question(qnum) 
    elif qnum == len(questions):
        print(qnum, len(questions))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
            score.change_text("You reached a score of " + str(points))
    time.sleep(.5)

questions = [
    ["How many Americans live with some form of mental illness?", ["1 in 5","1 in 10","1 in 100","1 in 1000"]],
    ["What is the most common mental illness in the U.S.?", ["Anxiety", "Depression", "Postpartum depression", "Bipolar disorder"]],
    ["Suicide is the __ leading cause of death among teens and young adults in the U.S.", ["Second", "Seventh", "First", "Fourth"]],
]




def show_question(qnum):
    kill()
    pos = [100, 150, 200, 250]
  
    random.shuffle(pos)

    Button((10, 100), "1. ", 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=None)
    Button((10, 150), "2. ", 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=None)
    Button((10, 200), "3. ", 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=None)
    Button((10, 250), "4. ", 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=None)

    Button((50, pos[0]), questions[qnum-1][1][0], 20, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=on_right)
    Button((50, pos[1]), questions[qnum-1][1][1], 20, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=on_false)
    Button((50, pos[2]), questions[qnum-1][1][2], 20, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=on_false)
    Button((50, pos[3]), questions[qnum-1][1][3], 20, "rblack on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,255),
        command=on_false)


def kill():
    for _ in buttons:
        _.kill()

qnum = 1
points = 0

num_question = Label(screen, str(qnum), 0, 0)
score = Label(screen, " ", 50, 300)
title = Label(screen, questions[qnum-1][0], 10, 60, 20, color="white")

def start_again():
    pass

def loop():
    global game_on
    show_question(qnum)
  
    #flag = False
    # while flag:
    #   for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #       if homeButt.collidepoint(pygame.mouse.get_pos()):
    #         gv.appState = "homeScreen"
    #         flag = True
    #       if exitButt.collidepoint(pygame.mouse.get_pos()):
    #         exit()
    quizInfinity = False
    while quizInfinity == False:
        screen.fill(0)
        homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
        exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
        screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if homeButt.collidepoint(pygame.mouse.get_pos()):
              gv.appState = "homeScreen"
              quizInfinity = True
            if exitButt.collidepoint(pygame.mouse.get_pos()):
              exit()
                   
    
        buttons.update()
        buttons.draw(screen)
        show_labels()   
        clock.tick(60)
        pygame.display.update()
    pygame.QUIT
    # homeButt = pygame.draw.rect(screen, 'pink', [0,0,400,50])
    # exitButt = pygame.draw.rect(screen, 'white', [400,0,50,50])
    # screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
    # screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
    # pygame.display.update()
    
if __name__ == '__main__':
    pygame.init()
    game_on = 1
    loop()