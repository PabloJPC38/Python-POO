from modLista import Lista
from modPersonal import Personal
import json
from os import path

class Menu:
    
    def menu(self):
        
        lista = Lista()
        user = Lista.validadarUsuario()
        lista.leerArchivoJSON(path.dirname(__file__) + "/personal.json")
        lista.mostrarElementos()
        band = True
        
        if user == "uTesorero":
            
            lista.gastos_sueldos_por_empleados(input("Ingrese DNI:"))
                
            respuesta = input("Desea consultar otro sueldo? (s/n):")
            
            while band:
                
                if respuesta == "s":
                    
                    lista.gastos_sueldos_por_empleados(input("Ingrese DNI:"))
                
                elif respuesta == "n":
                    
                    band = False
                
                else:
                    
                    print("Respuesta no válida!!!")
                    
                respuesta = input("Desea consultar otro sueldo? (s/n):")
                    
        else:       
        
            print("1 - Insertar un agente en la colección en una posición determinada")
            print("2 - Agregar un agente a la colección")
            print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agentes se encuentra almacenado")
            print("4 - Punto 4")
            print("5 - Punto 5")
            print("6 - Punto 6")
            print("7 - Punto 7")
            print("8 - Almacenar los objetos de la colección Lista en el archivo “personal.json”")
            print("9 - Modificar Basico")
            print("10 - Modificar Porcentaje por Cargo")
            print("11 - Modificar Porcentaje por Categoria")
            print("12 - Modificar Importe Extra")
            print("13 - Salir")
            
            op = input("Ingrese opción:")
            
            while(op != "13"):
                
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

                elif op == "9":
                    
                    lista.modificar_basico(input("Ingrese DNI:"),float(input("Ingrese nuevo sueldo básico:")))
                
                elif op == "10":
                    
                    lista.modificar_porcentaje_por_cargo(input("Ingrese DNI:"),float(input("Ingrese nuevo porcentaje:")))
                
                elif op == "11":
                    
                    lista.modificar_porcentaje_por_categoria(input("Ingrese DNI:"),float(input("Ingrese nuevo porcentaje:")))
                
                elif op == "12":
                
                    lista.modificar_importe_extra(input("Ingrese DNI:"),float(input("Ingrese nuevo importe extra:")))
                
                print("1 - Insertar un agente en la colección en una posición determinada")
                print("2 - Agregar un agente a la colección")
                print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agentes se encuentra almacenado")
                print("4 - Punto 4")
                print("5 - Punto 5")
                print("6 - Punto 6")
                print("7 - Punto 7")
                print("8 - Almacenar los objetos de la colección Lista en el archivo “personal.json”")
                print("9 - Modificar Basico")
                print("10 - Modificar Porcentaje por Cargo")
                print("11 - Modificar Porcentaje por Categoria")
                print("12 - Modificar Importe Extra")
                print("13 - Salir")

                op = input("Ingrese opción:")