from tkinter import Grid, StringVar, Tk,Frame,Button,messagebox,Label,Entry
from pytube import exceptions,YouTube
import urllib.request
from PIL import Image, ImageTk
import os

#Variables Globales
global colorOscuro
colorOscuro="#181818"

class VentanaLink(Frame):
    def __init__(self,master=None) -> None:
        super().__init__(master, bg="#223eba")
        self.master
        self.pack()
        self.view()
    
    def view(self):
        link=StringVar()
        #----------------------------
        self.f1=Frame(self,bg="#223eba")
        self.f1.pack()

        lblLink=Label(self.f1,text="Ingresar Link del Video:",width=30,height=1,font=(10),fg="white",bg="#223eba")
        lblLink.pack(pady=5)

        self.txtLink=Entry(self.f1,width=45,textvariable=link)
        self.txtLink.pack(side="bottom",padx=5,pady=5)
        #----------------------------
        self.f2=Frame(self,bg="#223eba")
        self.f2.pack()
        btnDescarga=Button(self.f2,text="Descargar",width=20,height=2,command=lambda:self.Descarga(link.get()),bg="#22c7ba")
        btnDescarga.pack(side="right",pady=10,padx=5)

        Button(self.f2,text="Cancelar",width=15,height=2,command=self.master.destroy,bg="#22c7ba").pack(side="left",pady=10,padx=5)
        
    def Descarga(self,url):
        if self.Comprobar(url):
            root2=Tk()
            root2.geometry("1000x200")
            root2.title("Ventana Video")
            ventana=VentantaVideoInformacion(root2,url)
            ventana.mainloop()

    def Comprobar(self,url=""):
        resultado=True
        try:
            video=YouTube(url)
            video.check_availability()
            if(video.age_restricted):
                messagebox.showerror(title="Restriccion de Edad",message="El video no esta disponible para descarga")
                resultado=False
        except(exceptions.VideoUnavailable, exceptions.RegexMatchError):
            messagebox.showerror(title="Error de Link",message="El link ingresado es Invalido")
            resultado=False
        except:
            messagebox.showerror(title="Error de Video",message="Error Desconocido")
            resultado=False
        finally:
            return resultado

class VentantaVideoInformacion(Frame):
    def __init__(self,master=None,link="") -> None:
        super().__init__(master,bg=colorOscuro)
        self.master=master
        self.video=YouTube(link)
        self.pack(expand=True,fill="both")
        self.view()
    
    def view(self):
        #Frame 1 Imagen
        self.f1=Frame(self,bg=colorOscuro)
        self.f1.grid(row=0,column=0,columnspan=2)
        self.mostrar_imagen()
        #Frame 2 Descripcion
        self.f2=Frame(self,bg=colorOscuro)
        self.f2.grid(row=0,column=2)
        self.mostrar_Informacion()
        #Columna Boton Descargar y Cancelar
        self.f3=Frame(self,bg=colorOscuro)
        self.f3.grid(row=0,column=3)
        self.mostrar_descarga()
        Grid.rowconfigure(self, 0, weight=1)
        for y in range(1,4):
            Grid.columnconfigure(self, y, weight=1)

    def mostrar_imagen(self):
        nombre="miniatura.jpg"
        file="\miniatura.jpg"
        link_jpg=self.video.thumbnail_url
        r=urllib.request.urlopen(link_jpg)
        f=open(nombre,"wb")
        f.write(r.read())
        f.close()
        direccion=os.getcwd()+file
        load = Image.open(direccion)
        load = load.resize((300,200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load,master=self.f1)
        img = Label(self.f1,image=render)
        img.image = render
        img.pack(expand=True,fill="both")
    
    def mostrar_Informacion(self):
        lblTitulo=Label(self.f2,text=self.video.title,font=10,fg="white",bg=colorOscuro)
        lblTitulo.grid(row=0,column=0)
        lblAutor=Label(self.f2,text=self.video.author,font=10,fg="white",bg=colorOscuro)
        lblAutor.grid(row=1,column=0)
        lblDuracion=Label(self.f2,text="Duracion: " + str(self.video.length/60) + " minutos",font=10,fg="white",bg=colorOscuro)
        lblDuracion.grid(row=2,column=0)
        for x in range(1,3):
            Grid.rowconfigure(self.f2, x, weight=1)
        Grid.columnconfigure(self.f2, 0, weight=1)

    def mostrar_descarga(self):
        self.lblEstado=Label(self.f3,text="Estado: No descargado",font=10,fg="white",bg=colorOscuro)
        self.lblEstado.pack(side="bottom",pady=10)
        btnDescargar=Button(self.f3,text="Descargar",width=20,height=4,font=1,fg="white",bg="#171131",command=lambda:self.descargar_Video())
        btnDescargar.pack(side="top",pady=10)

    def descargar_Video(self):
        valor=True
        try:
            self.video.streams.get_by_resolution("720p").download(fr"D:\de mati en disco d\Listas de Youtube\Videos Individuales")
        except:
            try:
                self.video.streams.get_by_resolution("360p").download(fr"D:\de mati en disco d\Listas de Youtube\Videos Individuales") 
            except:
                messagebox.showerror(title="Error al descargar",text="Un error inesperado no permite la descarga")
                valor=False
                  
        if valor:
            self.lblEstado.config(text="Estado: Descargado")   
        else:
            self.lblEstado.config(text="Estado: Error al Descargar")

def main():
    root=Tk()
    root.title("Programa de descarga video de Youtube")
    ventana=VentanaLink(root)
    ventana.mainloop()

if __name__=="__main__":
    main()