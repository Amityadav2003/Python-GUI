from tkinter import*
A=Tk()
A.geometry("844x634")
name= Label(A,text="User Name")
name.place(x=30,y=50)
email= Label(A,text="Email")
email.place(x=30,y=80)
password= Label(A,text="Password")
password.place(x=30,y=110)


e1=Entry(A)
e1.place(x=110,y=50)
e2=Entry(A)
e2.place(x=110,y=80)
e3=Entry(A)
e3.place(x=110,y=110)
    

A.mainloop()
