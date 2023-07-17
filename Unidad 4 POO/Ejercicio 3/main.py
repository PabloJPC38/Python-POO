import tkinter as tk
from tkinter import ttk, messagebox
import requests

class Aplication:
    
    
    def __init__(self) -> None:
        
        self.__ventana = tk.Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor de moneda')
        
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S)) # type: ignore
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        
        ttk.Label(mainframe, text="dólares").grid(column = 3, row = 2, pady = 10, padx = 1,sticky = (tk.W, tk.E)) # type: ignore
        self.__dolares = tk.StringVar()
        self.__dolares.trace('w', self.calcular)
        self.__dolaresEntry = tk.Entry(mainframe,width=7,textvariable=self.__dolares)
        self.__dolaresEntry.grid(column=2, row=2, pady = 10, padx = 10,sticky = (tk.W, tk.E))# type: ignore

        self.__resultado = ttk.Label(mainframe, text="")
        self.__resultado.grid(column=2, row=4, sticky=tk.S)
        
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy).grid(column=3, row=7, columnspan=2, pady=10)# type: ignore
    
        
        
        self.__ventana.mainloop()

    def cotizacion(self):
        
        url = "https://www.dolarsi.com/api/api.php?type=dolar"
        response = requests.get(url)
        data = response.json()
        cotizacion = data[0]['casa']['venta']
        return float(cotizacion.replace(',', '.'))
    
    
    def calcular(self, *args):
        
        if self.__dolaresEntry.get() != "":
            
            try:
                valor = self.cotizacion()
            
                self.__resultado.configure(text = f"es equivalente a {(float(self.__dolaresEntry.get()) * valor):.2f} pesos")
            
            except ValueError:
                
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
                self.__resultado.configure(text="")
        else:
            
            self.__resultado.configure(text="")
        

def testAPP():

    mi_app = Aplication()

if __name__ == '__main__':
    testAPP()