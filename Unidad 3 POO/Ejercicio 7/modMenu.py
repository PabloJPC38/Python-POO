from modLista import Lista
from modPersonal import Personal
import json
from os import path

class Menu:
    
    def menu(self):
        
        lista = Lista()
        lista.leerArchivoJSON(path.dirname(__file__) + "/personal.json")
        lista.mostrarElementos()
        
        print("1 - Insertar un agente en la colección en una posición determinada")
        print("2 - Agregar un agente a la colección")
        print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agentes se encuentra almacenado")
        print("4 - Punto 4")
        print("5 - Punto 5")
        print("6 - Punto 6")
        print("7 - Punto 7")
        print("8 - Almacenar los objetos de la colección Lista en el archivo “personal.json”")
        print("9 - Salir")
        
        op = input("Ingrese opción:")
        
        while(op != "9"):
            
            if op == "1":
                
                lista.insertarElemento(int(input("Ingrese posición:")),lista.crearAgente())
                
            elif op == "2":
                
                lista.agregarElemento(lista.crearAgente())
            
            elif op == "3":
                
                lista.mostrarElemento(int(input("Ingrese posición:")))
                
            elif op == "4":
            
                l = lista.docentes_investigadores(input("Ingrese carrera:"))
            
            elif op == "5":
                
                lista.contarCantidad(input("Ingrese área de investigación:"))
            
            elif op == "6":
                
                lista.listadoOrdenado(input("Ingrese carrera:"))
            
            elif op == "7":
                
                lista.listarDocentesInvestigadores(input("Ingresar categoría:"))
            
            elif op == "8":
                
                lista.guardarListaEnJSON("/Ejercicio 7/personal2.json")

            
            print("1 - Insertar un agente en la colección en una posición determinada")
            print("2 - Agregar un agente a la colección")
            print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agentes se encuentra almacenado")
            print("4 - Punto 4")
            print("5 - Punto 5")
            print("6 - Punto 6")
            print("7 - Punto 7")
            print("8 - Almacenar los objetos de la colección Lista en el archivo “personal.json”")
            print("9 - Salir")

            op = input("Ingrese opción:")