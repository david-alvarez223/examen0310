class Snowflake0310:
    # Inicializamos los atributos con valores vacíos o 0
    encargado = ""
    direccion = ""
    num_empleados = 0
    contacto = ""
    ciudad = ""
    email = ""
    id_cafe = 0

    # Función para mostrar los datos del nombre
    def mostrar_datos0310(self):
        print(f"Encargado: {self.encargado}")
        print(f"Direccion: {self.direccion}")
        print(f"Numero de empleados: {self.num_empleados}")
        print(f"Contacto: {self.contacto}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Email: {self.email}")
        print(f"Id del cafe: {self.id_cafe}")

    # Función para listar 5 empleados en una lista
    def Listar_empleados0310(self):
        lista_empleados = [
            "Alvarez", 
            "Juan", 
            "Ana", 
            "Luis", 
            "Maria"
        ]
        return lista_empleados

    # Función para crear una tupla de 5 reseñas
    def Tupla_reseñas0310(self):
        tupla_reseñas = (
            "Muy bueno", 
            "El mejor cafe del mundo", 
            "Un million de estrellas", 
            "Servicio 10/10", 
            "Muy recomendado"
        )
        return tupla_reseñas

    # Función para crear un diccionario del menu
    def Dicionario_menu0310(self):
        diccionario_menu = {
            "Cafe": 25,
            "Donitas": 50,
            "Galletitas": 20,
            "Te": 60,
            "Leche": 15
        }
        return diccionario_menu

    # Función para dar de alta
    def altas(self):
        print("Los datos se mostraron correctamente.")

    # Función para dar de baja
    def bajas(self):
        print("Los datos se borraron correctamente.")

# Creación del objeto
nombre = Snowflake0310()

# Asignación de datos a los atributos
nombre.encargado = "Alvarez"
nombre.direccion = "0310"
nombre.num_empleados = 5
nombre.contacto = "+52 656 123 4567"
nombre.ciudad = "Juarez"
nombre.email = "SnowflakeCafe@Email.com"
nombre.id_cafe = "21308051280310"

# Utilización de los objetos
# Mostrar datos del nombre
nombre.mostrar_datos0310()

# Llamadas a las funciones
print("\nLista de empleados:")
print(nombre.Listar_empleados0310())

print("\nTupla de reseñas:")
print(nombre.Tupla_reseñas0310())

print("\nDiccionario del menu:")
print(nombre.Dicionario_menu0310())

# Operaciones de alta y baja
nombre.altas()
nombre.bajas()