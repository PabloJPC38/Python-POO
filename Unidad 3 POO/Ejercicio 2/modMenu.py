from ctrlHelado import ManejadorHelado
from ctrlSabor import ManejadorSabor
from os import path
import itertools
class Menu:
    
    @staticmethod
    def menu():
        
        sabores = ManejadorSabor(path.dirname(__file__) + "/sabores.csv")
        helados = ManejadorHelado()
        
        print("1 - Registrar un helado vendido")
        print("2 - Mostrar el nombre de los 5 sabores de helado más pedidos")
        print("3 - Estimar el total de gramos vendidos")
        print("4 - Mostrar los sabores vendidos en un tamaño")
        print("5 - Determinar el importe total recaudado por la Heladería, por cada tipo de helado")
        print("6 - Salir")
        
        op = input("Ingrese opción:")
        
        while(op != "6"):
            
            if op == "1":
                
                helados.registrarHelado(sabores)
                
                """for h in helados.getHelado():
                    
                    print(h)"""
            
            elif op == "2":

                for clave, valor in itertools.islice(helados.saboresMasPedidos(sabores).items(), 5):
                    
                    print(f"{clave}({valor})")


            elif op == "3":
                
                id = int(input("Ingrese número de sabor:"))
                
                helados.totalGramosVendidos(id,sabores)
            
            elif op == "4":
                
                gramos = float(input("Ingrese tamaño de helado:"))
                helados.heladoPorGramos(gramos)
            
            elif op == "5":
                
                helados.importeTotalXGramos()
            
            
            print("1 - Registrar un helado vendido")
            print("2 - Mostrar el nombre de los 5 sabores de helado más pedidos")
            print("3 - Estimar el total de gramos vendidos")
            print("4 - Mostrar los sabores vendidos en un tamaño")
            print("5 - Determinar el importe total recaudado por la Heladería, por cada tipo de helado")
            print("6 - Salir")
        
            op = input("Ingrese opción:")