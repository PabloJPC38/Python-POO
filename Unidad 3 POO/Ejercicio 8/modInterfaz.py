from zope.interface import Interface, implementer


class Interfaz(Interface): # type: ignore
    
    def insertarElemento(self, posicion, elemento):
        
        pass
    
    def agregarElemento(self, elemento):
        
        pass
    
    def mostrarElemento(self, posicion):
        
        pass

class ITesorero(Interface): # type: ignore
    def gastos_sueldo_por_empleado(self, dni):
        pass

class IDirector(Interface): # type: ignore
    def modificar_basico(self, dni, nuevo_basico):
        pass

    def modificar_porcentaje_por_cargo(self, dni, nuevo_porcentaje):
        pass

    def modificar_porcentaje_por_categoria(self, dni, nuevo_porcentaje):
        pass

    def modificar_importe_extra(self, dni, nuevo_importe_extra):
        pass