from tkinter import *  
top = Tk()  
top.geometry("300x150")  
radio = IntVar()  
lbl = Label(text = "Favourite programming language:")  
lbl.pack()  
R1 = Radiobutton(top, text="C", variable=radio, value=1)  
R1.pack( anchor = W )  
  
R2 = Radiobutton(top, text="C++", variable=radio, value=2)  
                    
R2.pack( anchor = W )  
  
R3 = Radiobutton(top, text="Java", variable=radio, value=3)  
                   
R3.pack( anchor = W)  
  
label = Label(top)  
label.pack()  
top.mainloop()  
