from modVehiculo import Vehiculo


class Nodo:
    
    def __init__(self, vehiculo) -> None:
        
        self.__vehiculo = vehiculo
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        
        return self.__siguiente
    
    def getDato(self):
        
        return self.__vehiculo
    
    def __repr__(self) -> str:
        
        return f"vehiculo:{self.__vehiculo}"