from modSabor import Sabor

class Helado:
    
    def __init__(self, gramos, precio, sabor : list[Sabor]) -> None:
        
        self.__gramos = gramos
        self.__precio = float(precio)
        self.__sabor = sabor
    
    def getGramos(self):
        
        return self.__gramos
    
    def getPrecio(self):
        
        return self.__precio
    
    def getSabor(self):
        
        return self.__sabor
    
    def getNbreSabor(self):
        
        sabores = []
        
        for sabor in self.__sabor:
            
            sabores.append(sabor.getNbreSabor())
        
        return sabores
    
    def __repr__(self):
        
        return f"gramos:{self.__gramos} - precio:{self.__precio} - sabores:{self.__sabor}"