from re import S
from tkinter import Tk,Label,Button,Frame


"""def cambiar_panel(master):
    f1=Frame(master,width=400,height=400,bg="white")
    f1.grid(row=0,column=0)

def botonFrame(master=None):
    boton=Button(master,text="tocar",command=lambda:cambiar_panel(frame1),bg="red")
    boton.pack()"""

class ventana1(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=800,height=800,bg="orange")
        self.master=master
        self.pack(expand=True,fill="both")
        self.views()
    def views(self):
        self.f1=Frame(self,height=400,width=400,bg="red")
        self.f1.grid(row=0,column=0)

        self.f2=Frame(self,height=400,width=400,bg="green")
        self.f2.grid(row=0,column=1)

        self.elementos(self.f2)

        self.f3=Frame(self,height=400,width=400,bg="blue")
        self.f3.grid(row=1,column=0)

        self.f4=Frame(self,height=400,width=400,bg="black")
        self.f4.grid(row=1,column=1)

        for x in range(2):
            self.columnconfigure(x,weight=1)
            self.rowconfigure(x,weight=1)
    def elementos(self,master):
        self.boton=Button(master,text="tocar",height=3,width=20,command=lambda:self.cambiar_blanco())
        self.boton.pack()
    def cambiar_blanco(self):
        self.f5=Frame(self,height=400,width=400,bg="white")
        self.f5.grid(row=0,column=0)

if __name__=="__main__":
    root=Tk()
    ventana=ventana1(root)
    ventana.mainloop()
    
"""frame1=Frame(root,width=800,height=800,bg="orange")
frame1.pack()

f1=Frame(frame1,width=400,height=400,bg="green")
f1.grid(row=0,column=0)

f2=Frame(frame1,width=400,height=400,bg="red")
f2.grid(row=0,column=1)
botonFrame(f2)

f3=Frame(frame1,width=400,height=400,bg="blue")
f3.grid(row=1,column=0)

f4=Frame(frame1,width=400,height=400,bg="black")
f4.grid(row=1,column=1)"""

""""""


"""frame1.mainloop()"""