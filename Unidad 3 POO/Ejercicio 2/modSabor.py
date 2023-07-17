

class Sabor:
    
    def __init__(self, id, ingred, nbreSabor) -> None:
        
        self.__id = int(id)
        self.__ingred = ingred
        self.__nbreSabor = nbreSabor
    
    def getId(self):
        
        return self.__id
    
    def getNbreSabor(self):
        
        return self.__nbreSabor

    def __repr__(self):
        
        return f"{self.__nbreSabor}"