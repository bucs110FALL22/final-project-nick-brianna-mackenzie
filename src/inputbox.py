import pygame as pg
import src.globalVariable as gv
pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
font = pg.font.SysFont('Arial', 25)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    #print(self.text)
                    gv.feedbackText = self.text
                    self.text = ''
                    #print(gv.feedbackText)
                    if gv.appState == "feedbackScreen":
                      screen.blit(font.render(gv.feedbackText, True, (0,0,0)), (10, 200))
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
                

    def update(self):
        # Resize the box if the text is too long.
        width = max(360, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


def inputBoxDraw():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 180, 140, 32)
    input_boxes = [input_box1, input_box2]

    done = False
  
    while done == False:
        # make an if statement here for the quit and home buttons
        # if mousedown in quit, quit()
        # if mousedown in home, gv.appState = "homeScreen"

        homeButt = pg.draw.rect(screen, 'pink', [0,0,400,50])
        exitButt = pg.draw.rect(screen, 'white', [400,0,50,50])
        screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
              if homeButt.collidepoint(pg.mouse.get_pos()):
                gv.appState = "homeScreen"
                done = True
              if exitButt.collidepoint(pg.mouse.get_pos()):
                exit()
            for box in input_boxes:
                box.handle_event(event)
      
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)

def inputBoxDraw2():
    clock = pg.time.Clock()
    pg.draw.rect(screen, 'white', [50,100,360,32]) #draw bg of input
    input_box1 = InputBox(50, 100, 360, 32)
    input_boxes = [input_box1]

    done = False
  
    while done == False:
        # make an if statement here for the quit and home buttons
        # if mousedown in quit, quit()
        # if mousedown in home, gv.appState = "homeScreen"

        homeButt = pg.draw.rect(screen, 'pink', [0,0,400,50])
        exitButt = pg.draw.rect(screen, 'white', [400,0,50,50])
        screen.blit(font.render('Home', True, (0,0,0)), (200, 10))
        screen.blit(font.render('Exit', True, (0,0,0)), (400, 10))
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
              if homeButt.collidepoint(pg.mouse.get_pos()):
                gv.appState = "homeScreen"
                done = True
                
              if exitButt.collidepoint(pg.mouse.get_pos()):
                exit()
            
            for box in input_boxes:
                box.handle_event(event)
      
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)
    
if __name__ == '__main__':
    inputBoxDraw()
    pg.quit()