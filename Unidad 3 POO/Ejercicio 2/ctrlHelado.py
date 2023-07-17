from modHelado import Helado
from ctrlSabor import ManejadorSabor
from modSabor import Sabor
from csv import reader
import operator

class ManejadorHelado:
    
    def __init__(self) -> None:
    
        self.__helados : list[Helado] = []
        self.__gramos = [100,150,250,500,1000]
    
    def getHelado(self):
        
        return self.__helados
    
    def getGramos(self, index):
        
        return self.__gramos[index - 1]
    
    def mostrarGramos(self):
        
        print("Gramos:")
        for i, gramos in enumerate(self.__gramos):
            
            print(f"{i + 1} - {gramos}")
        
    def getPrecio(self, gramos):
        
        precio = 0
        
        if gramos == 100:
            
            precio = 100
        
        elif gramos == 150:
            
            precio = 200
        
        elif gramos == 250:
            
            precio = 500
        
        elif gramos == 500:
        
            precio = 900
            
        elif gramos == 1000:
            
            precio = 1500
        
        return precio
    
    #PRIMERA PARTE
    def registrarHelado(self, sabores : ManejadorSabor) -> None:

        cant_sabor = 0
        respuesta = ""
        
        op = ""
        
        
        respuesta = input("Desea registrar un helado?(s/n) :")
        
        while(respuesta != "n"):
            
            sabor : list[Sabor] = []
            sabores.mostrarSabores()
            sabor.append(sabores.getSabor(int(input("Ingresar opción:"))))
            cant_sabor += 1
            
            op = input("Desea agregar otro sabor?(s/n) :")
            
            while(cant_sabor <= 4 and op != "n"):
                
                sabor.append(sabores.getSabor(int(input("Ingresar opción:"))))
                cant_sabor += 1
                
                op = input("Desea agregar otro sabor?(s/n) :")
            
            cant_sabor = 0
            self.mostrarGramos()
            gramos = self.getGramos(int(input("Ingrese opción:")))
            self.__helados.append(Helado(gramos, self.getPrecio(gramos), sabor))
            
            respuesta = input("Desea registrar un helado?(s/n) :")
    
    #SEGUNDA PARTE
    def contarSabor(self, sabor):

        cant = sum(1 for helado in self.__helados if sabor in helado.getSabor())
        return cant
    
    def saboresMasPedidos(self, sabores : ManejadorSabor) -> dict:
        
        s : dict = {}
        
        for sabor in sabores.getSabores():
            
            s[sabor] = self.contarSabor(sabor)
        
        return dict(sorted(s.items(), key = operator.itemgetter(1), reverse = True))
    
    #TERCERA PARTE
    def gramosDelSabor(self, id):
        
        gramos = 0
        
        for helado in self.__helados:
            
            for sabor in helado.getSabor():
                
                if sabor.getId() == id:
                    
                    gramos += helado.getGramos() / len(helado.getSabor())

        return gramos
    
    def totalGramosVendidos(self, id, sabores : ManejadorSabor):
        
        gramos = self.gramosDelSabor(id)
        sabor = ManejadorSabor.saborID(id,sabores.getSabores())
        print(f"Se vendió {gramos} gramos de {sabor}")

    #CUARTA PARTE
    
    def heladoPorGramos(self, gramos):
        
        sabores = ([helado.getNbreSabor() for helado in self.__helados if helado.getGramos() == gramos])
        
        print(f"Los sabores vendidos en {gramos} gramos son:")
        for sabor in sabores:
            
            print(sabor)
            
    #QUINTA PARTE
    
    def importeTotalXTipo(self,gramos):
        
        importe = sum([helado.getPrecio() for helado in self.__helados if helado.getGramos() == gramos])
    
        return importe
    
    def importeTotalXGramos(self):
        
        importe = 0.0
        
        for gramos in self.__gramos:
            
            importe = self.importeTotalXTipo(gramos)
            
            print(f"Importe total para los helados de {gramos} gramos:${importe}")