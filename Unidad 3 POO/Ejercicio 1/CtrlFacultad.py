from modFacultad import Facultad
from modCarrera import Carrera
from csv import reader

class ManejadorFacultad:
    
    def __init__(self, ruta):
        
        self.__facultades = ManejadorFacultad.leerArchivo(ruta)
    
    
    def getFacultades(self):
        
        return self.__facultades
    
    
    def encontrarFacultad(self, cod):
        
        band, i, posi = True, 0, -1
        
        while(band and len(self.__facultades)):
            
            if self.__facultades[i].getCod() == cod:
                
                band = False
                posi = i
            
            else:
                
                i += 1
                
        return posi
    
    def mostrarCarreras(self, posi):
        
        carreras = self.__facultades[posi].getCarreras()
        
        print(f"Facultad:{self.__facultades[posi].getNbre()}")
        
        for c in carreras:
            
            print(f"Carrera:{c.getNbre()} - Duración:{c.getDuracion()}")

        
    def encontrarCarrera(self, nbre):
        
        band, i, j, posi, cod = True, 0, 0, 0, ""
        
        while band and i < len(self.__facultades):
            
            while band and j < len(self.__facultades[i].getCarreras()):
                
                if self.__facultades[i].getCarreras()[j].getNbre() == nbre:
                    
                    cod = self.__facultades[i].getCarreras()[j].getCod()
                    band = False
                
                else:
                    
                    j += 1

            i += 1
            j = 0
        
        print(f"Codigo:{cod[0]+cod} - Facultad:{self.__facultades[int(cod[0])-1].getNbre()} - Ubicación:{self.__facultades[int(cod[0])-1].getLocal()}")
    
    def Menu(self):
        
        print("1 - Mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad")
        print("2 - Mostrar código, nombre y localidad de la facultad donde esta se dicta una carrera")
        print("3 - Salir")
        
        op = input("Ingrese opción:")
        
        while(op != "3"):
            
            if op == "1":
                
                self.mostrarCarreras(self.encontrarFacultad(input("Ingrese código de la facultad:")))
            
            elif op == "2":
                
                self.encontrarCarrera(input("Ingrese nombre de la carrera:"))
            
            
            print("1 - Mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad")
            print("2 - Mostrar código, nombre y localidad de la facultad donde esta se dicta una carrera")
            print("3 - Salir")
        
            op = input("Ingrese opción:")

    @staticmethod
    def leerArchivo(ruta):
        
        facultades : list[Facultad] = []
        
        with open(ruta, "r", encoding="utf-8") as file:
            
            lineas = reader(file,delimiter=";")
            cod = "0"
            
            for l in lineas:
                
                if cod not in l[0]:
                    
                    f = Facultad(l[0],l[1],l[2],l[3],l[4])
                    facultades.append(f)
                    cod = l[0]
                
                else:
                    
                    facultades[int(cod) - 1].setCarreras(Carrera(l[0],l[1],l[2],l[3],l[4]))
        
        return facultades
