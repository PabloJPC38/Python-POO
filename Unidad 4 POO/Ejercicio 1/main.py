from tkinter import ttk, Tk, IntVar, DoubleVar, N, W, E, S, messagebox

class Aplicacion():
    
    def __init__(self) -> None:
        
        self.__ventana = Tk()
        self.__ventana.geometry('400x200')
        #ventana.configure(bg = 'grey')
        self.__ventana.title('Calculadora IPC')
        
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # type: ignore
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        #mainframe['relief'] = 'sunken'
        
        
        self.__entradas_cantidad = []
        self.__entradas_precio_base = []
        self.__entradas_precio_actual = []
        
        ttk.Label(mainframe, text="Item").grid(column=0, row=0, sticky=W)
        ttk.Label(mainframe, text="Vestimenta").grid(column=0, row=1, sticky=W)
        ttk.Label(mainframe, text="Alimentos").grid(column=0, row=2, sticky=W)
        ttk.Label(mainframe, text="Educación").grid(column=0, row=3, sticky=W)
        ttk.Label(mainframe, text="Cantidad").grid(column=1, row=0, sticky=W)
        ttk.Label(mainframe, text="Precio Año Base").grid(column=2, row=0, sticky=S)
        ttk.Label(mainframe, text="Precio Año Actual").grid(column=3, row=0, sticky=S)
        
        self.__resultado = ttk.Label(mainframe, text="IPC %  XX.XX  %")
        self.__resultado.grid(column=0, row=7, sticky=S)
        
        for i in range(3):
            
            cantidad_var = IntVar()
            precio_base_var = DoubleVar()
            precio_actual_var = DoubleVar()

            cantidad_entry = ttk.Entry(mainframe, width=7, textvariable=cantidad_var) 
            cantidad_entry.grid(column = 1, row = (i + 1), pady = 10, padx = 10, sticky = [W,E]) # type: ignore
            
            precio_base = ttk.Entry(mainframe, width=7, textvariable=precio_base_var) 
            precio_base.grid(column = 2, row = (i + 1), pady = 10, padx = 10, sticky = [W,E]) # type: ignore
            
            precio_actual = ttk.Entry(mainframe, width=7, textvariable=precio_actual_var) 
            precio_actual.grid(column = 3, row = (i + 1), pady = 10, padx = 10, sticky = [W,E]) # type: ignore
            
            
            self.__entradas_cantidad.append(cantidad_var)
            self.__entradas_precio_base.append(precio_base_var)
            self.__entradas_precio_actual.append(precio_actual_var)
            
        ttk.Button(mainframe, text="Calcular IPC", command=self.calcular_ipc).grid(column=1, row=7, columnspan=2, pady=10)
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy).grid(column=3, row=7, columnspan=2, pady=10)# type: ignore
    
        self.__ventana.mainloop()

    def calcular_ipc(self):
        
        try:
            resultados = []
            
            for i in range(len(self.__entradas_cantidad)):
                
                cantidad = self.__entradas_cantidad[i].get()
                precio_base = self.__entradas_precio_base[i].get()
                precio_actual = self.__entradas_precio_actual[i].get()

                if cantidad and precio_base and precio_actual:
                    cantidad = int(cantidad)
                    precio_base = float(precio_base)
                    precio_actual = float(precio_actual)

                    calculo = (precio_actual * cantidad) / (precio_base * cantidad) 
                    ipc = round(((calculo % 1) * 100), 2)
                    resultados.append(ipc)

            self.__resultado.configure(text = f"IPC % " + ", %".join(map(str, resultados)))

        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numéricos')


    
def testAPP():

    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()