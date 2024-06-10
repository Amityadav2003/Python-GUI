from tkinter import*
A=Tk()
A.geometry("844x634")
name= Label(A,text="User Name")
name.place(x=30,y=50)
email= Label(A,text="Email")
email.place(x=30,y=80)
password= Label(A,text="Password")
password.place(x=30,y=110)

A.mainloop()
