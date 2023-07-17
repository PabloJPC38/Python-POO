from modPersonal import Personal


class Nodo:
    
    def __init__(self, personal) -> None:
        
        self.__personal = personal
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        
        return self.__siguiente
    
    def getDato(self):
        
        return self.__personal
    
    def __repr__(self) -> str:
        
        return f"personal:{self.__personal}"