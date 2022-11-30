#import pygame
#from Rectangle import Rectangle
import tkinter as tk                    
from tkinter import ttk

class Surface:
  def __init__(self):
    website = tk.Tk()
    website.title("Mental Health Help")
    tabControl = ttk.Notebook(website)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)  
    tab4 = ttk.Frame(tabControl)
    
    tabControl.add(tab1, text ='Login/Sign Up')
    tabControl.add(tab5, text ='Data')
    tabControl.add(tab2, text ='Quiz')
    tabControl.add(tab3, text ='Resources')
    tabControl.add(tab4, text ='Feedback')
    tabControl.pack(expand = 1, fill ="both")
  
    ttk.Label(tab1, text ="Welcome").grid(column = 0, row = 0, padx =30, pady = 30)  
    ttk.Label(tab2,text ="Mental Health").grid(column = 0, row = 0, padx = 30,pady = 30)
    ttk.Label(tab3,text ="hey").grid(column = 0, row = 0, padx =   30,pady = 30)
    ttk.Label(tab4,text ="sup").grid(column = 0, row = 0, padx = 30,pady = 30)
    ttk.Label(tab5,text ="thisll have some stuff where you input data and it outputs a graph").grid(column = 0, row = 0, padx = 30,pady = 30)


   #  style = ttk.Style()

   #  style.theme_create( "colors", parent="alt", settings={ 
   # "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },    "TNotebook.Tab": { "configure": {"padding": [5, 1], "background": 'green' }, "map":       {"background":   [("selected", 'red')], "expand": [("selected", [1, 1, 1, 0])] } } } )
   #  style.theme_use("colors")
   #  root.mainloop()


    
    
    
    
  #   self.rect = Rectangle(x,y,height,width)
  #   self.image = filename
  #   surface = pygame.display.set_mode((400,300))
  #   color = (255,0, 0)
  #   surface.fill(color)
  #   pygame.display.flip()

  # def getRect(self):
  #   return self.rect