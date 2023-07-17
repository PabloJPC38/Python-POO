from ctrTaller import ManejadorTaller
from os import path

if __name__ == "__main__":
    
    talleres = ManejadorTaller(path.dirname(__file__) + "/talleres.csv")
    talleres.inscripcion()
    talleres.consultarInscripcion(input("Ingrese DNI:"))
    talleres.consultarInscriptos(int(input("Ingrese ID:")))
    talleres.registrarPago(input("Ingrese DNI:"))
    talleres.guardarInscripciones()