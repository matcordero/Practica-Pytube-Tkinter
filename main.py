from tkinter import Tk,Label,Button,Frame,Grid


"""def cambiar_panel(master):
    f1=Frame(master,width=400,height=400,bg="white")
    f1.grid(row=0,column=0)

def botonFrame(master=None):
    boton=Button(master,text="tocar",command=lambda:cambiar_panel(frame1),bg="red")
    boton.pack()"""

class ventana1(Frame):
    def __init__(self,master=None):
        super().__init__(master,bg="orange")
        self.master=master
        self.pack(expand=True,fill="both")
        self.views()
    def views(self):
        self.f1=Frame(self,bg="red")
        self.f1.grid(row=0,column=0,sticky='nsew')

        self.f2=Frame(self,bg="green")
        self.f2.grid(row=0,column=1,sticky='nsew')

        self.elementos()

        self.f3=Frame(self,bg="blue")
        self.f3.grid(row=1,column=0,sticky='nsew')

        self.f4=Frame(self,bg="black")
        self.f4.grid(row=1,column=1,sticky='nsew',columnspan=2,rowspan=2)

        for x in range(0,3):
            self.grid_rowconfigure(x,minsize=400,weight=1)
            self.grid_columnconfigure(x,minsize=400,weight=1)
            """Grid.columnconfigure(self,x,weight=1)
            Grid.rowconfigure(self,x,weight=1)"""
    def elementos(self):
        boton=Button(self.f2,text="tocar",command=lambda:self.cambiar_blanco())
        boton.pack(padx=200,pady=200)
    def cambiar_blanco(self):
        self.f1.destroy()
        self.f5=Frame(self,height=400,width=400,bg="white")
        self.f5.grid(row=0,column=0,sticky="nsew")

if __name__=="__main__":
    root=Tk()
    root.minsize(800,800)
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