from tkinter import *  
  
top = Tk()  
  
def hello():  
    print("hello!")  
  
# create a toplevel menu  
menubar = Menu(root)  
menubar.add_command(label="Hello!", command=hello)  
menubar.add_command(label="Quit!", command=top.quit)  
  
# display the menu  
top.config(menu=menubar)  
  
top.mainloop()  
