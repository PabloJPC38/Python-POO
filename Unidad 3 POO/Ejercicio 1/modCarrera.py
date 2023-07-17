

class Carrera:
    
    def __init__(self, cod, nbre, fecha, duracion, titulo) -> None:
        
        self.__cod = cod
        self.__nbre = nbre
        self.__fecha = fecha
        self.__duracion = duracion
        self.__titulo = titulo

    def getCod(self):
        
        return self.__cod
    
    def getNbre(self):
        
        return self.__nbre
    
    def getDuracion(self):
        
        return self.__duracion
    
    def __repr__(self):
        
        return f"{self.__cod} - {self.__nbre} - {self.__fecha} - {self.__duracion} - {self.__titulo}"