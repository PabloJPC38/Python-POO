from modColeccion import Coleccion


if __name__ == "__main__":
    
    c = Coleccion()
    
    """for empleados in c.getEmpleados():
        
        print(empleados)"""
    c.registrarHoras(input("Ingrese DNI:"), int(input("Ingrese horas acumuladas:")))
    c.totalTareas()
    c.ayudaEconomica()
    c.sueldos()