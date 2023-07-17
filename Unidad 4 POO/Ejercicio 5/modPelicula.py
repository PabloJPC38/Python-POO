


class Pelicula:
    
    def __init__(self, titulo, descrip, idioma, fecha, generos):
        self.__titulo = titulo
        self.__descrip = descrip
        self.__idioma = idioma
        self.__fecha = fecha
        self.__generos = generos
    
    def getTitulo(self):
        
        return self.__titulo
    
    def getDescrip(self):
        
        return self.__descrip
    
    def getIdioma(self):
        
        return self.__idioma
    
    def getFecha(self):
        
        return self.__fecha
    
    def getGeneros(self):
        
        return self.__generos
    
    