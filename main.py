from tkinter import *

def cambiar_panel(master):
    f1=Frame(master,width=400,height=400,bg="white")
    f1.grid(row=0,column=0)

def botonFrame(master=None):
    boton=Button(master,text="tocar",command=lambda:cambiar_panel(frame1),bg="red")
    boton.pack()

root=Tk()
frame1=Frame(root,width=800,height=800,bg="orange")
frame1.pack()

f1=Frame(frame1,width=400,height=400,bg="green")
f1.grid(row=0,column=0)

f2=Frame(frame1,width=400,height=400,bg="red")
f2.grid(row=0,column=1)
botonFrame(f2)

f3=Frame(frame1,width=400,height=400,bg="blue")
f3.grid(row=1,column=0)

f4=Frame(frame1,width=400,height=400,bg="black")
f4.grid(row=1,column=1)

""""""


frame1.mainloop()