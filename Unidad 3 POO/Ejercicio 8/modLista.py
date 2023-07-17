from modNodo import Nodo
from modInterfaz import Interfaz, ITesorero, IDirector
from zope.interface import implementer
from modPersonal import Personal, Docente, Docente_Investigador, Investigador, Personal_Apoyo
import json

@implementer(IDirector)
@implementer(ITesorero)
@implementer(Interfaz)
class Lista:

    def __init__(self):
        
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):

        self.__actual = self.__comienzo
        
        return self

    def __next__(self):
        
        if self.__actual is None:
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def modificar_basico(self, dni, nuevo_basico):
        
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index < self.__tope and nodo_actual is not None:
            
            if dni in nodo_actual.getDato().getCuil():
                
                nodo_actual.getDato().setSueldo(nuevo_basico)
                band = False
            
            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
    
    def modificar_porcentaje_por_cargo(self, dni, nuevo_porcentaje):
    
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index < self.__tope and nodo_actual is not None:
            
            if dni in nodo_actual.getDato().getCuil():
                
                nodo_actual.getDato().setPorcentaje(nuevo_porcentaje)
                nodo_actual.getDato().setSueldo(nodo_actual.getDato().calcularSueldo())
                band = False
            
            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1

    def modificar_porcentaje_por_categoria(self, dni, nuevo_porcentaje):
    
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index < self.__tope and nodo_actual is not None:
            
            if dni in nodo_actual.getDato().getCuil():
                
                nodo_actual.getDato().setPorcentaje(nuevo_porcentaje)
                nodo_actual.getDato().setSueldo(nodo_actual.getDato().calcularSueldo())
                band = False
            
            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1

    def modificar_importe_extra(self, dni, nuevo_importe_extra):
    
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index < self.__tope and nodo_actual is not None:
            
            
            if isinstance(nodo_actual.getDato(), Docente_Investigador):
            
                if dni in nodo_actual.getDato().getCuil():
                
                    nodo_actual.getDato().setImporte(nuevo_importe_extra)
                    band = False
            
            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
    
    def gastos_sueldos_por_empleados(self,dni):
        
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index < self.__tope and nodo_actual is not None:
            
            if dni in nodo_actual.getDato().getCuil():
                
                print(f"Sueldo:{nodo_actual.getDato().calcularSueldo()}")
                band = False
                
            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
    
    @staticmethod
    def validadarUsuario():
        
        user, password, band = "", "", True
        
        user = input("Ingrese usuario:")
        
        while user not in ["uTesorero" ,"uDirector"]:
            
            print("Usuario no válido!!")
            user = input("Ingrese usuario:")
        
        password = input("Ingrese contraseña:")
        
        while band:
            
            if user == "uTesorero" and password == "ag@74ck":
                
                band = False
            
            elif user == "uDirector" and password == "ufC77#!1":
                
                band = False
            
            else:
                
                print("Contraseña incorrecta!!")
                password = input("Ingrese contraseña:")
        
        return user

    @staticmethod
    
    def crearAgente():
        
        agente = None
        
        print("Seleccione el tipo de agente que desea crear:")
        print("1. Docente")
        print("2. Investigador")
        print("3. Docente Investigador")
        print("4. Personal de Apoyo")
    
        tipo_agente = int(input("Ingrese el número correspondiente al tipo de agente: "))
    
        cuil = input("Ingrese el CUIL del agente: ")
        nombre = input("Ingrese el nombre del agente: ")
        apellido = input("Ingrese el apellido del agente: ")
        sueldo_basico = float(input("Ingrese el sueldo básico del agente: "))
        antiguedad = int(input("Ingrese la antigüedad del agente: "))

        if tipo_agente == 1:
        
            carrera = input("Ingrese la carrera del docente: ")
            cargo = input("Ingrese el cargo del docente: ")
            catedra = input("Ingrese la cátedra del docente: ")
            
            agente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
    
        elif tipo_agente == 2:
        
            area_investigacion = input("Ingrese el área de investigación: ")
            tipo_investigacion = input("Ingrese el tipo de investigación: ")
            
            agente = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
    
        elif tipo_agente == 3:
        
            carrera = input("Ingrese la carrera del docente investigador: ")
            cargo = input("Ingrese el cargo del docente investigador: ")
            catedra = input("Ingrese la cátedra del docente investigador: ")
            area_investigacion = input("Ingrese el área de investigación: ")
            tipo_investigacion = input("Ingrese el tipo de investigación: ")
            categoria_incentivos = input("Ingrese la categoría en el programa de incentivos de investigación: ")
            importe_extra = float(input("Ingrese el importe extra por docencia e investigación: "))
            
            agente = Docente_Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        
        elif tipo_agente == 4:
            
            categoria = input("Ingrese la categoría del personal de apoyo: ")
            
            agente = Personal_Apoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
            
        else:
        
            print("Opción no válida.")
            return None

        return agente
    
    def agregarElemento(self, elemento):
        
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def insertarElemento(self, posicion, elemento):
        
        if posicion == 0:
            
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        
        else:
            
            nodo_anterior = None
            nodo_actual = self.__comienzo
            index = 0
            
            while index < posicion and nodo_actual is not None and posicion < self.__tope:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
                nodo = Nodo(elemento)
                nodo.setSiguiente(nodo_actual)
                nodo_anterior.setSiguiente(nodo)
        
        self.__tope += 1

        
    def mostrarElemento(self, posicion):
        
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= posicion and nodo_actual is not None and posicion < self.__tope:
            
            if index == posicion:
                
                band = False
                print(nodo_actual)
            
            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1

    def mostrarElementos(self):
        
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while index <= self.__tope and nodo_actual is not None:
            
            print(nodo_actual)

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.getSiguiente()
            index += 1
    
    
    def docentes_investigadores(self, carrera):
        
        lista : list[Personal] = []
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= self.__tope and nodo_actual is not None:
            
            if nodo_actual.getDato().getUsado():
                
                if nodo_actual.getDato().getCarrera() == carrera and nodo_actual.getDato().getCargo() == "Docente Investigador":
                    
                    lista.append(nodo_actual.getDato())
            
            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
        
        
        lista.sort()
        
        return lista

    def contarCantidad(self, area_inv):
        
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index, c1, c2 = 0, 0, 0
        
        while index <= self.__tope and nodo_actual is not None:
            
            if nodo_actual.getDato().getArea_Inv() == area_inv:
                
                if nodo_actual.getDato().getCargo() == "Docente Investigador":
                
                    c1 += 1
            
                elif nodo_actual.getDato().getCargo() == "Investigador":
                
                    c2 += 1

            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
        
        print(f"Docentes Investigados:{c1} - Investigadores:{c2}")
    
    @staticmethod
    def listado(lista : list[Personal]):
        
        lista_nueva = []
        
        for l in lista:
            
            lista_nueva.append(f"{l.getNbre()} - {l.getApe()} - {type(l)} - {l.getSueldo()}")
        
        return lista_nueva

    def listadoOrdenado(self, carrera):
        
        lista = []
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= self.__tope and nodo_actual is not None:
            
            lista.append(nodo_actual.getDato())
            
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.getSiguiente()
            index += 1
        
        
        lista.sort(key=lambda nodo_actual: nodo_actual.getDatos().getApe())
        
        return Lista.listado(lista)
    
    
    def listarDocentesInvestigadores(self, categoria):
        
        total = 0.0
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
    
        while index <= self.__tope and nodo_actual is not None:
            
            if nodo_actual.getDato().getCargo() == "Docente Investigador":
                
                if nodo_actual.getDato().getCategoria() == categoria:
                    
                    print(f"{nodo_actual.getDato().getApe()} - {nodo_actual.getDato().getNbre()} - {nodo_actual.getDato().getImporte()}")

                    total += nodo_actual.getDato().getImporte()
            
            else:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
    
        print(f"Total:{total}")


    def leerArchivoJSON(self, ruta_archivo):
    
        try:
            
            personal = None
            
            with open(ruta_archivo) as archivo:
            
                datos = json.load(archivo)
        
        except FileNotFoundError:
        
            print(f"El archivo no existe: {ruta_archivo}")
    
        except json.JSONDecodeError:
        
            print(f"El archivo no contiene datos JSON válidos: {ruta_archivo}")
        
        else:
            
            for dato in datos:
            
                tipo_personal = dato["tipo_personal"]
                cuil = dato["cuil"]
                apellido = dato["apellido"]
                nombre = dato["nombre"]
                sueldo_basico = dato["sueldo_basico"]
                antiguedad = dato["antiguedad"]
            
                if tipo_personal == "Docente":
                
                    carrera = dato["carrera"]
                    cargo = dato["cargo"]
                    catedra = dato["catedra"]
                    
                    personal = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
            
                elif tipo_personal == "Investigador":
                
                    area_investigacion = dato["area_investigacion"]
                    tipo_investigacion = dato["tipo_investigacion"]
                    
                    personal = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
            
                elif tipo_personal == "Docente_Investigador":
                
                    carrera = dato["carrera"]
                    cargo = dato["cargo"]
                    catedra = dato["catedra"]
                    area_investigacion = dato["area_investigacion"]
                    tipo_investigacion = dato["tipo_investigacion"]
                    categoria_incentivos = dato["categoria_incentivos"]
                    importe_extra = dato["importe_extra"]
                
                    personal = Docente_Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
            
                elif tipo_personal == "Personal_Apoyo":
                
                    categoria = dato["categoria"]
                    
                    personal = Personal_Apoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
                
                else:
                
                    print(f"Tipo de personal no válido: {tipo_personal}")
                
                self.agregarElemento(personal)

    def guardarListaEnJSON(self, ruta_archivo):
        
        datos = None
        
        lista_codificada = []

        for elemento in self:
            
            if isinstance(elemento, Docente):
                tipo_personal = 'Docente'
                datos = {
                    'tipo_personal': tipo_personal,
                    'cuil': elemento.getCuil(),
                    'apellido': elemento.getApe(),
                    'nombre': elemento.getNbre(),
                    'sueldo_basico': elemento.getSueldo(),
                    'antiguedad': elemento.getAntig(),
                    'carrera': elemento.getCarrera(),
                    'cargo': elemento.getCargo(),
                    'catedra': elemento.getCatedra()
                }

            elif isinstance(elemento, Investigador):
            
                tipo_personal = 'Investigador'
                datos = {
                    'tipo_personal': tipo_personal,
                    'cuil': elemento.getCuil(),
                    'apellido': elemento.getApe(),
                    'nombre': elemento.getNbre(),
                    'sueldo_basico': elemento.getSueldo(),
                    'antiguedad': elemento.getAntig(),
                    'area_investigacion': elemento.getArea_Inv(),
                    'tipo_investigacion': elemento.getTipoInv()
                }

            elif isinstance(elemento, Docente_Investigador):
            
                tipo_personal = 'Docente_Investigador'
                datos = {
                    'tipo_personal': tipo_personal,
                    'cuil': elemento.getCuil(),
                    'apellido': elemento.getApe(),
                    'nombre': elemento.getNbre(),
                    'sueldo_basico': elemento.getSueldo(),
                    'antiguedad': elemento.getAntig(),
                    'carrera': elemento.getCarrera(),
                    'cargo': elemento.getCargo(),
                    'catedra': elemento.getCatedra(),
                    'area_investigacion': elemento.getArea_Inv(),
                    'tipo_investigacion': elemento.getTipoInv(),
                    'categoria_incentivos': elemento.getCategoria(),
                    'importe_extra': elemento.getImporte()
                }

            elif isinstance(elemento, Personal_Apoyo):
                
                tipo_personal = 'Personal_Apoyo'
                datos = {
                    'tipo_personal': tipo_personal,
                    'cuil': elemento.getCuil(),
                    'apellido': elemento.getApe(),
                    'nombre': elemento.getNbre(),
                    'sueldo_basico': elemento.getSueldo(),
                    'antiguedad': elemento.getAntig(),
                    'categoria': elemento.getCategoria()
                }

            else:
            
                print("Tipo de personal no válido.")

            lista_codificada.append(datos)

        with open("personal2.json", 'w') as archivo:
            
            json.dump(lista_codificada, archivo, indent=4)

    def __repr__(self) -> str:
        
        return f"actual:{self.__actual} - comienzo:{self.__comienzo}"