from os import path
from csv import reader
from modEmpleados import Empleado, Externos, Contratados, Planta
import numpy as np

class Coleccion:
    
    def __init__(self) -> None:
        
        self.__empleados = Coleccion.leerArchivos()
    
    
    def getEmpleados(self):
        
        return self.__empleados
    
    
    def registrarHoras(self, dni, horas):
        
        band, i = True, 0

        while(band and len(self.__empleados)):
            
            if isinstance(self.__empleados[i], Contratados) and dni == self.__empleados[i].getDNI():
                
                print(f"Horas acumuladas antes:{self.__empleados[i].getHoras()}")
                self.__empleados[i].setHoras(horas)
                print(f"Horas acumuladas actualizadas:{self.__empleados[i].getHoras()}")
                band = False    
            
            else:
                
                i += 1
    
    def totalTareas(self):
        
        band, i = True, 0

        while(band and len(self.__empleados)):
            
            if isinstance(self.__empleados[i], Externos) and self.__empleados[i].obraNoTerminada():
                
                print(f"Costo de obra:{self.__empleados[i].getCosto()}")
                band = False
            
            else:
                
                i += 1

    def ayudaEconomica(self):
        
        print("Empleados que tendrán ayuda económica:")
        
        for empleado in self.__empleados:
            
            if empleado.Sueldo() < 150000:
                
                print(f"{empleado.getNbre()} - {empleado.getDir()} - {empleado.getDNI()}")
    
    
    def sueldos(self):
        
        print("Sueldos:")
        
        for empleado in self.__empleados:
            
            print(f"{empleado.getNbre()} - {empleado.getTel()} - ${empleado.Sueldo()}")
    
    @staticmethod
    def lenArchivo(ruta):
        
        with open(ruta, "r", encoding = "utf-8") as file:
            
            next(file)
            lineas = reader(file, delimiter = ";")
            
            dim = sum (1 for _ in lineas)
            
            return dim
            
    @staticmethod
    def dimension(rutas : list):
        
        dim = 0
        
        for ruta in rutas:
            
            dim += Coleccion.lenArchivo(ruta)
        
        return dim
    
    @staticmethod
    def leerArchivo(ruta, empleados, j):
        
        posi = 0
        
        with open(ruta, "r", encoding = "utf-8") as file:
            
            next(file)
            
            for i, line in enumerate(file):
                # Dividir la línea por el delimitador ';'
                val = line.strip().split(';')

                if "planta" in ruta:
                    
                    empleado = Planta(val[0], val[1], val[2], val[3],val[4], val[5])
                    
                elif "contratados" in ruta:
                    
                    empleado = Contratados(val[0], val[1], val[2], val[3],val[4], val[5], val[6])
                    empleado.setValor_Hora(val[7])
                    
                else:
                    
                    empleado = Externos(val[0], val[1], val[2], val[3],val[4], val[5], val[6], val[7], val[8], val[9])
                
                empleados[i + j] = empleado
                posi = i + j
                
            return posi + 1
        
    @staticmethod
    def leerArchivos():
        
        ruta1 = path.dirname(__file__) + "/planta.csv"
        ruta2 = path.dirname(__file__) + "/contratados.csv"
        ruta3 = path.dirname(__file__) + "/externos.csv"
        
        posi = 0
        
        dim = Coleccion.dimension([ruta1,ruta2,ruta3])
        
        empleados = np.empty(dim, dtype = Empleado)
        
        for ruta in [ruta1,ruta2,ruta3] :
            
            posi = Coleccion.leerArchivo(ruta, empleados, posi)

        return empleados