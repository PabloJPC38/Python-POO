import unittest
from modLista import Lista
from modVehiculo import Vehiculo

class TestAutomatizado(unittest.TestCase):

    def setUp(self):
        self.lista = Lista()
        
    def test_agregar_vehiculo(self):
        vehiculo = Vehiculo(True, "Marca4", "Modelo4", 2, "Blanco", 22000)
        self.lista.agregarElemento(vehiculo)

        self.assertEqual(self.lista.getTope(), 1)
    
    def test_insertar_vehiculo(self):
        # Prueba de inserción en la posición 0
        vehiculo1 = Vehiculo(True, "Marca1", "Modelo1", 4, "Rojo", 20000)
        self.lista.insertarElemento(0, vehiculo1)
        self.assertEqual(self.lista.mostrarElemento(0), vehiculo1)
        
        # Prueba de inserción en una posición intermedia
        vehiculo2 = Vehiculo(False, "Marca2", "Modelo2", 2, "Azul", 15000)
        vehiculo3 = Vehiculo(True, "Marca5", "Modelo5", 2, "Negro", 22000)
        self.lista.agregarElemento(vehiculo3)
        self.lista.insertarElemento(1, vehiculo2)
        self.assertEqual(self.lista.mostrarElemento(1), vehiculo2)
        
         # Prueba de inserción en la última posición
        vehiculo4 = Vehiculo(True, "Marca3", "Modelo3", 4, "Negro", 18000)
        self.lista.insertarElemento(self.lista.getTope(), vehiculo4)

        self.assertEqual(self.lista.getTope(), 4)

    def test_mostrar_elemento(self):
            
        vehiculo5 = Vehiculo(False, "Marca5", "Modelo5", 4, "Gris", 17000)
        self.lista.agregarElemento(vehiculo5)
        self.assertEqual(self.lista.mostrarElemento(0), vehiculo5)
            
    def test_modificar_precio(self):
            
        vehiculo6 = Vehiculo(True, "Marca3", "Modelo3", 4, "Negro", 18000,"","AABBCC",2010)
        self.lista.agregarElemento(vehiculo6)
        precio_venta_anterior = vehiculo6.importeVenta()
        precio_venta_posterior = self.lista.modificarPrecio("AABBCC")
        
        self.assertNotEqual(precio_venta_anterior,precio_venta_posterior)
if __name__ == "__main__":
    unittest.main()
