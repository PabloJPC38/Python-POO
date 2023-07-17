from modPelicula import Pelicula
import requests

# Configuración de la API
API_KEY = "b7bded61da66f6319d2e2bdc93f9e1eb"
API_URL = "https://api.themoviedb.org/3"


class manejadorPelicula:
    
    def __init__(self) -> None:
        
        self.__peliculas : list[Pelicula] = self.cargarPeliculas()
    
    
    def obtenerPeliculas(self):
        
        url = f"{API_URL}/discover/movie?api_key={API_KEY}&language=es"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        peliculas = data.get("results", [])
        
        return peliculas

    def cargarPeliculas(self):
        
        peliculas : list[Pelicula] = []
        
        for p in self.obtenerPeliculas():
            
            titulo = p.get("title")
            resumen = p.get("overview")
            idioma = p.get("original_language")
            fecha = p.get("release_date")
            generos_ids = p.get("genre_ids", [])
            generos = self.getGenerosPelicula(generos_ids)
            
            pelicula = Pelicula(titulo, resumen, idioma, fecha, generos)
            
            peliculas.append(pelicula)
        
        return peliculas
            
    def getGenerosPelicula(self, genre_ids):
        
        url = f"{API_URL}/genre/movie/list?api_key={API_KEY}&language=es"
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        generos_dict = {genero["id"]: genero["name"] for genero in data.get("genres", [])}
        generos = [generos_dict.get(genre_id) for genre_id in genre_ids]
        
        return generos
        
    def getPeliculas(self):
        
        return self.__peliculas
    
