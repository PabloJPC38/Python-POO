from modTaller import Taller
from modInscripcion import Incripcion
from datetime import datetime
from modPersona import Persona
from csv import reader, writer
import numpy as np

class ManejadorTaller:
    
    def __init__(self, ruta) -> None:
        
        self.__talleres = ManejadorTaller.leerArchivo(ruta)
        self.__inscripciones = []
    
    def getTalleres(self):
        
        return self.__talleres
    
    def getTaller(self):
        
        for i, taller in enumerate(self.__talleres):
            
            print(f"{i+1} - {taller.getNbre()}")
    
    def vacanteTaller(self, index):
        
        vacante = False
        
        if self.__talleres[index].getVacante() != 0:
            
            self.__talleres[index].setVacante()
            vacante = True
        
        return vacante
    
    
    def inscripcion(self):
        
        respuesta = input("Desea inscribirse a un taller? (s/n) :")
        band = True
        i = 0
        nbre, dir, dni = "", "", ""
        dnis = []
        
        while band:
            
            if respuesta == "s":
                
                self.getTaller()
                
                i = int(input("Ingrese taller:"))
                
                if self.vacanteTaller(i - 1):
            
                    print(f"Hay vacantes!!")
                    
                    
                    nbre = input("Ingrese nombre de la persona:")
                    dir = input("Ingrese dirección:")
                    dni = input("Ingrese DNI:")

                    while dni in dnis:
                        
                        print("No se puede inscribir a otro taller")
                        nbre = input("Ingrese nombre de la persona:")
                        dir = input("Ingrese dirección:")
                        dni = input("Ingrese DNI:")
                    
                    dnis.append(dni)
                    
                    persona = Persona(nbre,dir,dni)
            
                    inscripcion = Incripcion(datetime.now().date(),False,persona,self.getTalleres()[i - 1])
                    
                    print(f"Incripto al taller '{self.getTalleres()[i - 1].getNbre()}'!!")
                    
                    self.__inscripciones.append(inscripcion)
                    
                    respuesta = input("Desea inscribirse a un taller? (s/n) :")
                    
                else:
            
                    print(f"No hay más vacantes para el taller '{self.getTalleres()[i - 1].getNbre()}'!!)")
            
            elif respuesta == "n":
                
                band = False
            
            
    
    def consultarInscripcion(self, dni):
        
        band, i = True, 0
        
        while(band and i < len(self.__inscripciones)):
            
            if self.__inscripciones[i].getPersona().getDNI() == dni:
                
                print(f"Taller:{self.__inscripciones[i].getTaller().getNbre()} - Monto:{self.__inscripciones[i].getTaller().getMonto()}")
                band = False
            
            else: 
                
                i += 1
        
        if band and i == len(self.__inscripciones):
            
            print("No se encuentra inscripta esa persona en ningún taller")

    def posicionTaller(self, id):
        
        band, i, posi= True, 0, 0

        while(band and i < len(self.__inscripciones)):
            
            if self.__inscripciones[i].getTaller().getId() == id:
                
                posi = i
                band = False

            else:
                
                i += 1
        
        return posi
    
    def consultarInscriptos(self, id):
        
        print("Incriptos:")
        for inscripcion in self.__inscripciones:
            
            if inscripcion.getTaller().getId() == id:
                
                print(f"{inscripcion.getPersona()}")
    
    def posicionPesona(self, dni):
        
        band, i, posi= True, 0, 0

        while(band and i < len(self.__inscripciones)):
            
            if self.__inscripciones[i].getPersona().getDNI() == dni:
                
                posi = i
                band = False

            else:
                
                i += 1
        
        return posi
    
    def registrarPago(self, dni):
        
        if self.__inscripciones[self.posicionPesona(dni)].getPago():
            
            print("Ya pagó esta persona!!")
            
        else:
        
            self.__inscripciones[self.posicionPesona(dni)].setPago(True)
            print("Pago realizado!!")

    def guardarInscripciones(self):
        
        with open("copia.csv", "w", newline='') as file:
            
            write = writer(file)
            
            for ins in self.__inscripciones:
                
                write.writerow([ins.getPersona().getDNI(),ins.getTaller().getId(),ins.getFecha(),ins.getPago()])
                
    @staticmethod
    def dimension(ruta: str):
        with open(ruta, "r", encoding = "utf-8") as file:
        
            # Contar la cantidad de líneas restantes
            lineas = sum(1 for _ in file)
        
            return lineas

            
    @staticmethod
    def leerArchivo(ruta: str):

        # Obtener la dimensión del archivo CSV
        dim = ManejadorTaller.dimension(ruta)

        # Crear un arreglo vacío de tipo object con la dimensión obtenida
        talleres = np.empty(dim, dtype = Taller)

        with open(ruta, "r", encoding="utf-8", errors="ignore") as file:

            # Leer línea por línea y crear objetos de la clase Alumno
            for i, line in enumerate(file):
                # Dividir la línea por el delimitador ';'
                values = line.strip().split(';')

                # Crear un objeto Alumno con los valores de la línea
                taller = Taller(values[0], values[1], values[2], values[3])

                # Guardar el objeto Alumno en el arreglo de NumPy
                talleres[i] = taller

        return talleres