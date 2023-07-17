from __future__ import annotations
from datetime import date


class Vehiculo:
    
    def __init__(self, usado, marca, modelo, puertas, color, precio, version = "", patente = "", anio = 0, kilometraje = 0) -> None:
        
        self.__usado = usado
        self.__marca = marca
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio = float(precio)
        self.__version = version
        self.__patente = patente
        self.__anio = int(anio)
        self.__kilometraje = int(kilometraje)
    
    
    def getUsado(self):
        
        return self.__usado
    
    def getMarca(self):
        
        return self.__marca
    
    def getModelo(self):
        
        return self.__modelo
    
    def getPuertas(self):
        
        return self.__puertas
    
    def getColor(self):
        
        return self.__color
    
    def getPrecio(self):
        
        return self.__precio
    
    def getVersion(self):
        
        return self.__version
    
    def getAnio(self):
        
        return self.__anio
    
    def getKilometraje(self):
        
        return self.__kilometraje
    
    def setPrecio(self, precio):
    
        self.__precio = precio
    
    def getPatente(self):
        
        return self.__patente
    
    def importeVenta(self):
        
        importe = 0.0
        anio_actual = int(date.today().year)
        
        if self.__usado:
            
            if self.__kilometraje > 100000:
        
                importe = self.__precio - ((self.__precio * 0.01) * (anio_actual - self.__anio)) - (self.__precio * 0.02)

            else:
                
                importe = self.__precio - ((self.__precio * 0.01) * (anio_actual - self.__anio))
        
        else:
            
            if self.__version == "full":
                
                importe = self.__precio + (self.__precio * 0.1) + (self.__precio * 0.02)
            
            else:
                
                importe = self.__precio + (self.__precio * 0.1)
        
        return importe
    
    def __gt__(self, otro : Vehiculo):
        
        return self.importeVenta() > otro.importeVenta()
    
    def __repr__(self) -> str:
        
        return f"{self.__usado} - {self.__marca} - {self.__modelo} - {self.__puertas} - {self.__color}"