import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application=tk.Tk()
main_application.geometry('1200*800')
main_application.title('vaibhav text editor')

################################## main menu ##############################################
main_menu = tk.Menu()

file = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
colour_theme = tk.Menu(main_menu, tearoff=False)
help = tk.Menu(main_menu, tearoff=False)

# cascade
main_menu.add_cascade(labels='File', menu=file)
main_menu.add_cascade(labels='Edit', menu=edit)
main_menu.add_cascade(labels='View', menu=view)
main_menu.add_cascade(labels='Colour_theme', menu=colour_theme)
main_menu.add_cascade(labels='Help', menu=help)
#-----------------------&&&&&&&&&& End main menu &&&&&&&&&----------------------------------


################################## Toolbar ##############################################
#-----------------------&&&&&&&&&& End main menu &&&&&&&&&----------------------------------


################################## text editor ##############################################
#-----------------------&&&&&&&&&& End main menu &&&&&&&&&----------------------------------


################################## main status bar ##############################################
#-----------------------&&&&&&&&&& End main menu &&&&&&&&&----------------------------------

################################## main menu functionality ##############################################

main_application.config(menu=main_menu)
main_application.mainloop()




#-----------------------&&&&&&&&&& End main menu &&&&&&&&&----------------------------------