from datetime import datetime


class Empleado:
    
    def __init__(self, dni, nbre, dir, tel) -> None:
        
        self.__dni = dni
        self.__nbre = nbre
        self.__dir = dir
        self.__tel = tel
    
    def getDNI(self):
        
        return self.__dni
    
    def getNbre(self):
        
        return self.__nbre
    
    def getDir(self):
        
        return self.__dir
    
    def getTel(self):
        
        return self.__tel
    
    def Sueldo(self):
        
        pass
    
    def __repr__(self) -> str:
        
        return f"dni:{self.__dni} - nombre:{self.__nbre} - dirección:{self.__dir} - teléfono:{self.__tel}"
    
    

class Planta(Empleado):
    
    def __init__(self, dni, nbre, dir, tel, sueldo_basico, antig) -> None:
        
        self.__sueldo_basico = float(sueldo_basico)
        self.__antig = int(antig)
        super().__init__(dni, nbre, dir, tel)

    def getSueldo_Basico(self):
        
        return self.__sueldo_basico
    
    def getAntig(self):
        
        return self.__antig
    
    def Sueldo(self):
        
        return self.__sueldo_basico +((self.__sueldo_basico / 100) * self.__antig)
    
    def __repr__(self) -> str:
        return super().__repr__() + f" - sueldo_basico:{self.__sueldo_basico} - antig:{self.__antig}"
    
class Contratados(Empleado):
    
    __valor_hora = 0.0
    
    def __init__(self, dni, nbre, dir, tel, f_inicio, f_fin, horas) -> None:
        
        self.__f_inicio = f_inicio
        self.__f_fin = f_fin
        self.__horas = int(horas)
        
        super().__init__(dni, nbre, dir, tel)
    
    def getF_Inicio(self):
        
        return self.__f_inicio
    
    def getF_Fin(self):
        
        return self.__f_fin
    
    def setHoras(self, horas):
        
        self.__horas += horas
    
    def getHoras(self):
        
        return self.__horas
    
    def Sueldo(self):
        
        return self.__horas * Contratados.__valor_hora
    
    @classmethod    
    def setValor_Hora(cls, valor):
        
        cls.__valor_hora = float(valor)
    
    def __repr__(self) -> str:
        return super().__repr__() + f" - f_inicio:{self.__f_inicio} - f_fin:{self.__f_fin} - horas:{self.__horas} - valor:{Contratados.__valor_hora}"

class Externos(Empleado):
    
    def __init__(self, dni, nbre, dir, tel, tarea, f_inicio, f_fin, monto_viatico, costo, monto_vida) -> None:
        
        self.__tarea = tarea
        self.__f_inicio = f_inicio
        self.__f_fin = f_fin
        self.__monto_viatico = float(monto_viatico)
        self.__costo = float(costo)
        self.__monto_vida = float(monto_vida)
        
        super().__init__(dni, nbre, dir, tel)
    
    def obraNoTerminada(self) -> bool:
        
        respuesta = False
        
        date = datetime.today()
        
        fecha = date.strftime("%Y-%m-%d")
        
        if fecha < self.__f_fin:
            
            respuesta = True

        return respuesta
    
    def getTarea(self):
        
        return self.__tarea
    
    def getF_Inicio(self):
        
        return self.__f_inicio
    
    def getF_Fin(self):
        
        return self.__f_fin
    
    def getMontoViatico(self):
        
        return self.__monto_viatico
    
    def getCosto(self):
        
        return self.__costo
    
    def getMontoVida(self):
        
        return self.__monto_vida
    
    def Sueldo(self):
        
        return self.__costo - self.__monto_viatico - self.__monto_vida

    def __repr__(self) -> str:
        return super().__repr__() + f" - tarea:{self.__tarea} - f_inicio:{self.__f_inicio} - f_fin:{self.__f_fin} - monto_viatico:{self.__monto_viatico} - costo:{self.__costo} - monto_vida:{self.__monto_vida}"
