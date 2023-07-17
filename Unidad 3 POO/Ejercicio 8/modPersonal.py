from __future__ import annotations


class Personal:
    
    def __init__(self, cuil, ape, nbre, sueldo, antig) -> None:
        
        self.__cuil = cuil
        self.__ape = ape
        self.__nbre = nbre
        self.__sueldo = float(sueldo)
        self.__antig = int(antig)
    
    def calcularSueldo(self):
        
        sueldo = self.__sueldo + (self.__sueldo * float(self.__antig / 100))
        
        return sueldo
    
    def getCuil(self):
        
        return self.__cuil
    
    def getApe(self):
        
        return self.__ape
    
    def getNbre(self):
        
        return self.__nbre
    
    def setSueldo(self, sueldo):
        
        self.__sueldo = sueldo
    
    def getSueldo(self):
        
        return self.__sueldo
    
    def getAntig(self):
        
        return self.__antig

    def __lt__(self, otro : Personal):
        
        return self.__nbre < otro.__nbre
    
    def __repr__(self) -> str:
        
        return f"{self.__cuil} - {self.__ape} - {self.__nbre} - ${self.__sueldo} - {self.__antig} años"
    
    
class Docente(Personal):
    
    def __init__(self, cuil, ape, nbre, sueldo, antig, carrera, cargo, catedra) -> None:
        
        Personal.__init__(self,cuil, ape, nbre, sueldo, antig)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        self.__porcent1 = 0.1
        self.__porcent2 = 0.2
        self.__porcent3 = 0.5
        
        
    def calcularSueldo(self):
        
        sueldo = 0.0
        
        if self.__cargo == "simple":
        
            sueldo = super().calcularSueldo() + (self.getSueldo() * self.__porcent1)

        elif self.__cargo == "semiexclusivo":
            
            sueldo = super().calcularSueldo() + (self.getSueldo() * self.__porcent2)
            
        elif self.__cargo == "exclusivo":
            
            sueldo = super().calcularSueldo() + (self.getSueldo() * self.__porcent3)
        
        return sueldo
    
    def setPorcentaje(self, porcentaje):
        
        self.__porcent1 = porcentaje / 100
        
        self.__porcent1 = (porcentaje + 2) / 100
        
        self.__porcent1 = (porcentaje + 5) / 100
    
    def getCarrera(self):
        
        return self.__carrera
    
    def getCargo(self):
        
        return self.__cargo
    
    def getCatedra(self):
        
        return self.__catedra
    
    def __repr__(self) -> str:
        return super().__repr__() + f" - {self.__carrera} - {self.__cargo} - {self.__catedra}"
    
    
class Investigador(Personal):
    
    def __init__(self, cuil, ape, nbre, sueldo, antig, area_inv, tipo_inv) -> None:
        
        Personal.__init__(self,cuil, ape, nbre, sueldo, antig)
        self.__area_inv = area_inv
        self.__tipo_inv = tipo_inv

    def calcularSueldo(self):
        return super().calcularSueldo()
    
    def getArea_Inv(self):
    
        return self.__area_inv
    
    def getTipoInv(self):
        
        return self.__tipo_inv
    
    def __repr__(self) -> str:
        return super().__repr__() + f" - {self.__area_inv} - {self.__tipo_inv}"


class Personal_Apoyo(Personal):
    
    def __init__(self, cuil, ape, nbre, sueldo, antig, categoria) -> None:
        
        Personal.__init__(self,cuil, ape, nbre, sueldo, antig)
        self.__categoria = categoria
        self.__porcent1 = 0.1
        self.__porcent1 = 0.2
        self.__porcent1 = 0.3
    
    def setPorcentaje(self, porcentaje):
        
        self.__porcent1 = porcentaje / 100
        
        self.__porcent1 = (porcentaje + 2) / 100
        
        self.__porcent1 = (porcentaje + 3) / 100
    
    def calcularSueldo(self):
        
        sueldo = 0.0
        
        if self.__categoria in range(1,11):
        
            sueldo = super().calcularSueldo() + (self.getSueldo() * 0.1)
        
        elif self.__categoria in range(11,21):
        
            sueldo = super().calcularSueldo() + (self.getSueldo() * 0.2)
        
        elif self.__categoria in range(21,23):
        
            sueldo = super().calcularSueldo() + (self.getSueldo() * 0.3)

        return sueldo
    
    def getCategoria(self):
        
        return self.__categoria
    
    def __repr__(self) -> str:
        return super().__repr__() + f" - {self.__categoria}"

class Docente_Investigador(Docente, Investigador):
    
    def __init__(self, cuil, ape, nbre, sueldo, antig, carrera, cargo, catedra, area_inv, tipo_inv, categoria, importe):
        
        #super().__init__(cuil, ape, nbre, sueldo, antig, carrera, cargo, catedra)
        Docente.__init__(self,cuil, ape, nbre, sueldo, antig, carrera, cargo, catedra)
        Investigador.__init__(self,cuil, ape, nbre, sueldo, antig, area_inv, tipo_inv)
        self.__categoria = categoria
        self.__importe = importe
        

    def calcularSueldo(self):
        
        return Docente.calcularSueldo(self) + self.__importe
    
    def getCategoria(self):
        
        return self.__categoria
    
    def setImporte(self, importe):
        
        self.__importe = importe
    
    def getImporte(self):
        
        return self.__importe
    
    def __repr__(self) -> str:
        
        categoria = self.getCategoria()
        importe = self.getImporte()
        
        return super().__repr__() + f" - {categoria} - ${importe}"