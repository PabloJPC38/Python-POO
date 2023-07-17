import tkinter as tk
from tkinter import ttk



class Aplication:
    
    
    def __init__(self) -> None:
        
        self.__ventana = tk.Tk()
        self.__ventana.geometry('250x300')
        self.__ventana.title('Calculo de IVA')
        
        
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S)) # type: ignore
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        
        ttk.Label(mainframe, text="Precio sin IVA").grid(column = 2, row = 2, pady = 10, padx = 10,sticky = (tk.W, tk.E)) # type: ignore
        ttk.Label(mainframe, text=" IVA").grid(column = 2, row = 5, pady = 10, padx = 10,sticky = (tk.W, tk.E)) # type: ignore
        ttk.Label(mainframe, text="Precio con IVA").grid(column = 2, row = 6, pady = 10, padx = 10,sticky = (tk.W, tk.E)) # type: ignore
        
        self.__precio = tk.DoubleVar()
        self.__precioEntry = ttk.Entry(mainframe,width=7,textvariable=self.__precio)
        self.__precioEntry.grid(column=4, row=2, pady = 10, padx = 40,sticky = (tk.W, tk.E)) # type: ignore
        
        
        self.__porcent = tk.DoubleVar()
        
       
        labelframe = ttk.Frame(mainframe)
        labelframe.grid(column=2, row=3, columnspan=3, pady=10, padx=10, sticky=(tk.W, tk.E))# type: ignore
        labelframe.configure(borderwidth=0, relief='flat')
        
        ttk.Radiobutton(labelframe,text='IVA 21%', value = 21, variable = self.__porcent).grid(column=1,row =3, pady=5, padx=10, sticky=(tk.W, tk.E))# type: ignore
        ttk.Radiobutton(labelframe,text='IVA 10.5%', value = 10.5, variable = self.__porcent).grid(column=1,row =4,pady=5, padx=10, sticky=(tk.W, tk.E))# type: ignore
        
        self.__IVA = tk.DoubleVar()
        self.__IVAEntry = ttk.Entry(mainframe,width=7, state='readonly',textvariable=self.__IVA)
        self.__IVAEntry.grid(column=4, row=5, pady = 10, padx = 40,sticky = (tk.W, tk.E)) # type: ignore
        
        self.__precioIVA = tk.DoubleVar()
        self.__precioIVAEntry = ttk.Entry(mainframe,width=7, state='readonly',textvariable=self.__precioIVA)
        self.__precioIVAEntry.grid(column=4, row=6, pady = 10, padx = 40,sticky = (tk.W, tk.E)) # type: ignore
        
        
        style = ttk.Style()
        style.configure('calcular.TButton', foreground='black', background='green')
        style.configure('salir.TButton', foreground='black', background='red')
        
        ttk.Button(mainframe, text="Calcular", command=self.calcular_IVA,style='calcular.TButton').grid(column=1, row=7, columnspan=2, pady=10)
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy, style='salir.TButton').grid(column=3, row=7, columnspan=2, pady=10)# type: ignore
    
        
        self.__ventana.mainloop()
    
    def calcular_IVA(self):
        
        self.__IVA.set(self.__precio.get() * self.__porcent.get() / 100)
        self.__precioIVA.set(self.__precio.get() + self.__IVA.get())
        
        
def testAPP():

    mi_app = Aplication()

if __name__ == '__main__':
    
    testAPP()