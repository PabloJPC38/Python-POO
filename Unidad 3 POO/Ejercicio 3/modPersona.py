


class Persona:
    
    def __init__(self, nbre, dir, dni) -> None:
        
        self.__nbre = nbre
        self.__dir = dir
        self.__dni = dni
    
    def getNbre(self):
        
        return self.__nbre
    
    def getDNI(self):
        
        return self.__dni

    def __repr__(self):
        
        return f"nbre:{self.__nbre} - dni:{self.__dni}"