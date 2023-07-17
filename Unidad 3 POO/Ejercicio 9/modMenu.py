from modLista import Lista
from modVehiculo import Vehiculo
import json
from os import path

class Menu:
    
    def menu(self):
        
        lista = Lista()
        lista.leerArchivoJSON(path.dirname(__file__)+"/vehiculos.json")
        lista.mostrarElementos()
        
        print("1 - Insertar un vehículo en la colección en una posición determinada")
        print("2 - Agregar un vehículo a la colección")
        print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado")
        print("4 - Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta")
        print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
        print("6 - Mostrar para todos los vehículos")
        print("7 - Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”")
        print("8 - Salir")
        
        op = input("Ingrese opción:")
        
        while(op != "8"):
            
            if op == "1":
                
                respuesta = input("Es usado:(s/n):")
                
                if respuesta == "s":
                    
                    usado = True
                    marca = input("Ingrese marca:")
                    modelo = input("Ingrese modelo:")
                    puertas = int(input("Ingrese n° de puertas:"))
                    color = input("Ingrese color:")
                    precio = float(input("Ingrese precio"))
                    patente = input("Ingrese patente:")
                    anio = int(input("Ingrese año:"))
                    kilometraje = int(input("Ingrese kilometraje:"))
                    
                    lista.insertarElemento(int(input("Ingrese posición:")),Vehiculo(usado,marca,modelo,puertas,color,precio,"",patente,anio,kilometraje))
                
                elif respuesta == "n":
                    
                    usado = False
                    marca = input("Ingrese marca:")
                    modelo = input("Ingrese modelo:")
                    puertas = int(input("Ingrese n° de puertas:"))
                    color = input("Ingrese color:")
                    precio = float(input("Ingrese precio:"))
                    version = input("Ingrese version:")
                    
                    lista.insertarElemento(int(input("Ingrese posición:")),Vehiculo(usado,marca,modelo,puertas,color,precio,version))
                
            elif op == "2":
                
                respuesta = input("Es usado:(s/n):")
                
                if respuesta == "s":
                    
                    usado = True
                    marca = input("Ingrese marca:")
                    modelo = input("Ingrese modelo:")
                    puertas = int(input("Ingrese n° de puertas:"))
                    color = input("Ingrese color:")
                    precio = float(input("Ingrese precio:"))
                    patente = input("Ingrese patente:")
                    anio = int(input("Ingrese año:"))
                    kilometraje = int(input("Ingrese kilometraje:"))
                
                    lista.agregarElemento(Vehiculo(usado,marca,modelo,puertas,color,precio,"",patente,anio,kilometraje))

                elif respuesta == "n":
                    
                    usado = False
                    marca = input("Ingrese marca:")
                    modelo = input("Ingrese modelo:")
                    puertas = int(input("Ingrese n° de puertas:"))
                    color = input("Ingrese color:")
                    precio = float(input("Ingrese precio:"))
                    version = input("Ingrese version:")
                    
                    lista.agregarElemento(Vehiculo(usado,marca,modelo,puertas,color,precio,version))

                
                
            elif op == "3":
                
                lista.mostrarElemento(2)
                
            elif op == "4":
            
                lista.modificarPrecio(input("Ingrese patente:"))
            
            elif op == "5":
                
                lista.masEconomico()
            
            elif op == "6":
                
                lista.mostrarElementos()
            
            elif op == "7":
                
                lista.guardarListaEnJSON(path.dirname(__file__)+"/vehiculos2.json")

            
            print("1 - Insertar un vehículo en la colección en una posición determinada")
            print("2 - Agregar un vehículo a la colección")
            print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado")
            print("4 - Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta")
            print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
            print("6 - Mostrar para todos los vehículos")
            print("7 - Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”")
            print("8 - Salir")
            
            op = input("Ingrese opción:")