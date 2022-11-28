import tkinter as tk                    
from tkinter import ttk
  
  
root = tk.Tk()
root.title("Mental Health Help")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)  
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Login/Sign Up')
tabControl.add(tab2, text ='Quiz')
tabControl.add(tab3, text ='Resources')
tabControl.add(tab4, text ='Feedback')
tabControl.pack(expand = 1, fill ="both")
  
ttk.Label(tab1, text ="Welcome").grid(column = 0, row = 0, padx =30, pady = 30)  
ttk.Label(tab2,text ="Mental Health").grid(column = 0, row = 0, padx = 30,pady = 30)
ttk.Label(tab3,text ="hey").grid(column = 0, row = 0, padx = 30,pady = 30)
ttk.Label(tab4,text ="sup").grid(column = 0, row = 0, padx = 30,pady = 30)


style = ttk.Style()

style.theme_create( "colors", parent="alt", settings={ 
 "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } }, "TNotebook.Tab": { "configure": {"padding": [5, 1], "background": 'green' }, "map":       {"background": [("selected", 'red')], "expand": [("selected", [1, 1, 1, 0])] } } } )
style.theme_use("colors")
root.mainloop()  