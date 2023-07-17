from modPelicula import Pelicula
from gestorPelicula import manejadorPelicula
from modVista import Ventana

class controladorPelicula(object):
    
    def __init__(self) -> None:
        
        self.__peliculas = manejadorPelicula()
        self.__vista = Ventana(self)
    
    def obtenerPelicula(self,index):
        
        return self.__peliculas.getPeliculas()[index]
    
    def mostrarTitulos(self):
        
        titulos = [pelicula.getTitulo() for pelicula in self.__peliculas.getPeliculas()]
        
        return titulos
    
    def star(self):
    
        self.__vista.mainloop()