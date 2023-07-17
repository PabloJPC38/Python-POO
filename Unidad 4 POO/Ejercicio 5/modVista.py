import tkinter as tk
from tkinter import ttk


class listaPelicula(ttk.Frame):
    
    def __init__(self, master, mostrador, ctrlPeli, **kwargs):
        
        super().__init__(master)
        
        self.__lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command= self.__lb.yview)
        self.__lb.config(yscrollcommand=scroll.set)
        scroll.pack(side= tk.RIGHT, fill= tk.Y)
        self.__lb.pack(expand= True, fill = tk.BOTH)
        
        self.__lb.bind("<Double-Button-1>", lambda event: self.mostrarDetalles(event, ctrlPeli))

        
        self.mostrarTitulos(ctrlPeli)
        
        self.__mostrador = mostrador
        
    def mostrarTitulos(self,ctrlPeli):
        
        titulos = ctrlPeli.mostrarTitulos()
        
        for titulo in titulos:
            
            
            self.__lb.insert(tk.END, titulo)
            self.__lb.itemconfig(tk.END, foreground="blue")
            self.__lb.itemconfig(tk.END, selectforeground="white", selectbackground="blue")

    def mostrarDetalles(self, event,ctrlPeli):
        
        index = self.__lb.curselection()[0]
        
        pelicula = ctrlPeli.obtenerPelicula(index)
        
        self.__mostrador.mostrarPelicula(pelicula)
    
class Mostrador(ttk.LabelFrame):
    
    def __init__(self, master, **kwargs):
        
        super().__init__(master, text="Película", **kwargs)
        
        self.__titulo = tk.StringVar()
        self.__resumen = ttk.Label(self, wraplength=400, justify="left")
        self.__idioma = tk.StringVar()
        self.__fecha = tk.StringVar()
        self.__generos = tk.StringVar()

        ttk.Label(self, textvariable=self.__titulo).pack(padx=10, pady=5)
        self.__resumen.pack(padx=10, pady=5)
        ttk.Label(self, textvariable=self.__idioma).pack(padx=10, pady=5)
        ttk.Label(self, textvariable=self.__fecha).pack(padx=10, pady=5)
        ttk.Label(self, textvariable=self.__generos).pack(padx=10, pady=5)
        
    def mostrarPelicula(self, pelicula):
        self.__titulo.set(f"Título: {pelicula.getTitulo()}")
        self.__resumen.config(text=f"Descripción: {pelicula.getDescrip()}")
        self.__idioma.set(f"Idioma original: {pelicula.getIdioma()}")
        self.__fecha.set(f"Fecha de lanzamiento: {pelicula.getFecha()}")
        self.__generos.set(f"Género: {pelicula.getGeneros()}")   

class Ventana:
    
    def __init__(self,ctrlPeli):
        
        self.__ventana = tk.Tk()
        self.__ventana.geometry("650x300")
        self.__ventana.title("Cinéfilos Argentinos")
        self.__mostrador = Mostrador(self.__ventana, width = 500, height = 240)
        self.__mostrador.place(x= 150, y=5)
        self.__list = listaPelicula(self.__ventana,self.__mostrador,ctrlPeli,width= 20, height = 14, borderwidth = 2, relief = "sunken")
        self.__list.place(x=5, y=6)

    def mainloop(self):
        
        self.__ventana.mainloop()
