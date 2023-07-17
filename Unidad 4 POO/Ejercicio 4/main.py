import tkinter as tk
from tkinter import ttk
from functools import partial


class Imaginario:
    def __init__(self, real, imaginario):
        self.__real = int(real)
        self.__imaginario = int(imaginario)
    
    def __str__(self):
        return f"{self.__real}+{self.__imaginario}i"
    
    def __add__(self, otro):
        
        
        real = self.__real + otro.__real
        imaginario = self.__imaginario + otro.__imaginario
        
        return Imaginario(real, imaginario)
        
    def __sub__(self, otro):
        
        real = self.__real - otro.__real
        imaginario = self.__imaginario - otro.imaginario
        
        return Imaginario(real, imaginario)
    
    def __mul__(self, otro):
        
        real = self.__real * otro.__real - self.__imaginario * otro.__imaginario
        imaginario = self.__real * otro.__imaginario + self.__imaginario * otro.__real
        
        return Imaginario(real, imaginario)
    
    def __truediv__(self, otro):
        
        divisor = otro.__real**2 + otro.__imaginario**2
        real = (self.__real * otro.__real + self.__imaginario * otro.__imaginario) / divisor
        imaginario = (self.__imaginario * otro.__real - self.__real * otro.__imaginario) / divisor
        
        return Imaginario(real, imaginario)


class Calculadora(object):
   
    def __init__(self):
        
        self.__ventana = tk.Tk()
        self.__ventana.title('Tk-Calculadora')
        
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))  # type: ignore
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        
        self.__panel = tk.StringVar()
        self.__operador = tk.StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(tk.W,tk.E))# type: ignore
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(tk.W,tk.E))# type: ignore
        
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=tk.W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=tk.W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=tk.W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=tk.W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=tk.W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=tk.W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=tk.W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=tk.W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=tk.W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=tk.W)
        ttk.Button(mainframe, text='i', command=partial(self.ponerImaginario)).grid(column=1, row=8, sticky=tk.W)
        
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=tk.W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=tk.W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=tk.W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=tk.W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=tk.W)
        
        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()
        
    def ponerNUMERO(self, numero):
        
        if self.__operadorAux==None:
            
            if "i" in self.__panel.get():
                
                aux = self.__panel.get()
                aux = aux.replace("i","")
                valor = aux + numero
                valor = valor + "i"
                self.__panel.set(valor)
                
            else:
                
                valor = self.__panel.get()
                self.__panel.set(valor+numero)
            
        else:
            
            if "i" in self.__panel.get():
                
                self.__operadorAux=None
                valor=self.__panel.get()
                real = valor.split("+")[0]
                posi = valor.find("+")
                print(f"REAL:{real}")
                print(f"posi:{posi}")
                imagin = valor[posi+1:].split("i")[0]
                
               
                print(f"IMAGINARIO:{imagin}")
                self.__primerOperando = Imaginario(real,imagin)
                self.__panel.set(numero)
                
            else:
                
                self.__operadorAux=None
                valor=self.__panel.get()
                self.__primerOperando=int(valor)
                self.__panel.set(numero)
            
    def ponerImaginario(self):
        
        valor = self.__panel.get() + "+i"
        self.__panel.set(valor)
    
    def borrarPanel(self):
        self.__panel.set('0')
    
    def resolverOperacion(self, operando1, operacion, operando2):
        
        resultado=0
        
        
        if operacion=='+':
            
            resultado=operando1+operando2
        
        else:
            
            if operacion=='-':
                
                resultado=operando1-operando2
            
            else:
                
                if operacion=='*':
                    
                    resultado=operando1*operando2
                
                else:
                    
                    if operacion=='/':
                        
                        resultado=operando1/operando2
        
        self.__panel.set(str(resultado))
    
    def ponerOPERADOR(self, op):
        if op=='=':
            
            if "i" in self.__panel.get():
            
                valor=self.__panel.get()
                real = valor.split("+")[0]
                print(f"REAL:{real}")
                posi = valor.find("+")
                print(f"posi:{posi}")
                imagin = valor[posi+1:].split("i")[0]
                print(f"IMAGINARIO:{imagin}")
                
                self.__segundoOperando = Imaginario(real,imagin)
                operacion=self.__operador.get()
                
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
            
            else:
            
                operacion=self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
        else:
            
            if self.__operador.get()=='':
                
                self.__operador.set(op)
                self.__operadorAux=op
            
            else:
                operacion=self.__operador.get()
                
                if "i" in self.__panel.get():
                    
                    valor=self.__panel.get()
                    real = valor.split("+")[0]
                    posi = valor.find("+")
                    imagin = valor[posi+1:].split("i")[0]
                    print(f"REAL:{real}")
                    print(f"IMAGINARIO:{imagin}")
                    self.__segundoOperando = Imaginario(real,imagin)
                    
                    self.__segundoOperando = self.__panel.get()
                    self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                    self.__operador.set(op)
                    self.__operadorAux=op
                
                else:
                    
                    self.__segundoOperando=int(self.__panel.get())
                    self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                    self.__operador.set(op)
                    self.__operadorAux=op
                    
def main():
    calculadora=Calculadora()
    
if __name__=='__main__':
    main()


