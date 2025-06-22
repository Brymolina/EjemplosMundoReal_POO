# reservando habitación en el hotel Juan Sebástian en Atacames

class Habitacion:
    def __init__(self, numero, tipo, precio):
        # atributos de la habitación
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False # la habitación esta libre

# aqui reservaremos una habitación
    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

# liberamos una habitación
    def liberar(self):
        self.ocupada = False
        print(f"Habitación {self.numero} ahora está disponible.")

# clase que representa un cliente del hotel
class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

# aqui realizando el método que permite al cliente reservar una habitación
    def reservar_habitacion(self, habitacion):
        if not habitacion.ocupada:
            habitacion.reservar()
            print(f"{self.nombre} ha reservado la habitación {habitacion.numero}.")
        else:
            print(f"{self.nombre}, la habitación {habitacion.numero} no está disponible.")


# Creando dos habitaciones
habitacion1 = Habitacion(101, "Individual", 50)
habitacion2 = Habitacion(102, "Doble", 80)

# Creando cliente
cliente1 = Cliente("Bryan Molina","1312244005")

# Reservando habitación
cliente1.reservar_habitacion(habitacion1)

# Intentamos reservarla de nuevo (habitación ocupada)
cliente1.reservar_habitacion(habitacion1)

# se libera la habitación
habitacion1.liberar()
cliente1.reservar_habitacion(habitacion1)