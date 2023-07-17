from modSabor import Sabor
from csv import reader

class ManejadorSabor:
    
    def __init__(self, ruta) -> None:
    
        self.__sabores = ManejadorSabor.leerArchivo(ruta)
    
    
    def getSabores(self):
        
        return self.__sabores
    
    def getSabor(self, index) -> Sabor:
        
        return self.__sabores[index - 1]
    
    def mostrarSabores(self):
        
        print("Sabores:")
        for i, sabor in enumerate(self.__sabores):
            
            print(f"{i + 1} - {sabor.getNbreSabor()}")
    
    @staticmethod
    def saborID(id, sabores : list[Sabor]):
        
        i, sabor, band = 0, "", True
        
        
        while i < len(sabores) and band:
            
            if sabores[i].getId() == id:
                
                sabor = sabores[i].getNbreSabor()
                band = False
            else:
                
                i += 1
        
        return sabor
            
    @staticmethod
    def leerArchivo(ruta):
        
        with open(ruta, "r", encoding = "utf-8") as file:
    
            return list(map(lambda l : Sabor(l[0],l[1], l[2]), reader(file, delimiter = ";")))