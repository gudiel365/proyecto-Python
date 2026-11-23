# CLASE BASE:
# Define los datos y métodos que comparten todas las mascotas.
class Mascota:
    # CONSTRUCTOR: recibe los datos iniciales al crear el objeto.
    def __init__(self, nombre, edad, tipo):
        self._nombre = ""
        self._edad = 0
        self.tipo = tipo
        self.estado = "Disponible"

        # Usamos los métodos de cambio para validar los datos iniciales.       
        self.set_nombre(nombre)
        self.set_edad(edad)

    # ENCAPSULAMIENTO:
    # Estos métodos permiten consultar los atributos privados.                    
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad
 
    # ENCAPSULAMIENTO Y VALIDACIÓN:
    # Solo acepta nombres que no estén vacíos.
    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre.strip()

    # Solo acepta edades que sean cero o mayores.
    def set_edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = nueva_edad

    def mostrar_info(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad, "años")
        print("Tipo:", self.tipo)
        print("Estado:", self.estado)

    def cambiar_estado(self):
        # MODIFICAR un dato del objeto.
        if self.estado == "Disponible":
            self.estado = "Adoptada"
        else:
            self.estado = "Disponible"


# HERENCIA:
# Perro hereda los atributos y métodos de Mascota.
class Perro(Mascota):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Perro")

    # POLIMORFISMO:
    # Perro muestra información adicional con este método.
    def mostrar_info(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad, "años")
        print("Tipo: Perro")
        print("Estado:", self.estado)
        print("Cuidados: necesita paseos.")

 
# HERENCIA:
# Gato también hereda de Mascota.
class Gato(Mascota):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Gato")

    # POLIMORFISMO:
    # Gato usa el mismo método, pero muestra otros cuidados.
    def mostrar_info(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad, "años")
        print("Tipo: Gato")
        print("Estado:", self.estado)
        print("Cuidados: necesita arenero limpio.")


# FUNCIÓN REUTILIZABLE:
# Busca una mascota por nombre y devuelve el objeto encontrado.
def buscar_mascota(lista, nombre):
    for mascota in lista:
        if mascota.get_nombre().lower() == nombre.lower():
            return mascota
    return None


# FUNCIÓN REUTILIZABLE CON MANEJO DE ERRORES:
# Sigue preguntando hasta recibir una edad entera válida.
def pedir_edad():
    while True:
        try:
            edad = int(input("Edad en años: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
            else:
                return edad
        except ValueError:
            print("Escribe la edad usando un número entero.")


def iniciar_programa():
    # LISTA DE OBJETOS:
    # Creamos objetos y los guardamos en una lista.
    mascotas = [
        Perro("Luna", 2),
        Perro("Max", 4),
        Gato("Michi", 1)
    ]

    # Esta lista guardará los objetos favoritos.
    favoritas = []

    # MENÚ Y CICLO:
    # El menú se repite hasta que la persona elige salir.
    while True:
        print("\n--- CATÁLOGO DE MASCOTAS ---")
        print("1. Mostrar mascotas")
        print("2. Buscar mascota")
        print("3. Agregar mascota a Favoritos")
        print("4. Mostrar Favoritos")
        print("5. Cambiar estado de adopción")
        print("6. Agregar una mascota")
        print("7. Ver reporte")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        # CONDICIONALES: cada opción realiza una acción distinta.
        if opcion == "1":
            # RECORRER y MOSTRAR los objetos de la lista.
            for mascota in mascotas:
                print("\n--------------------")
                mascota.mostrar_info()

        elif opcion == "2":
            nombre = input("Nombre que deseas buscar: ")
            mascota = buscar_mascota(mascotas, nombre)

            if mascota is None:
                print("No se encontró esa mascota.")
            else:
                print("\n--- Mascota encontrada ---")
                mascota.mostrar_info()

        elif opcion == "3":
            nombre = input("Nombre de la mascota: ")
            mascota = buscar_mascota(mascotas, nombre)

            if mascota is None:
                print("No se encontró esa mascota.")
            elif mascota in favoritas:
                print("Esa mascota ya está en Favoritos.")
            else:
                # AGREGAR un objeto a otra lista.
                favoritas.append(mascota)
                print("Mascota agregada a Favoritos.")

        elif opcion == "4":
            if len(favoritas) == 0:
                print("Todavía no tienes mascotas favoritas.")
            else:
                for mascota in favoritas:
                    print("\n--------------------")
                    mascota.mostrar_info()

        elif opcion == "5":
            nombre = input("Nombre de la mascota que deseas modificar: ")
            mascota = buscar_mascota(mascotas, nombre)

            if mascota is None:
                print("No se encontró esa mascota.")
            else:
                mascota.cambiar_estado()
                print("Nuevo estado:", mascota.estado)

        elif opcion == "6":
            # AGREGAR un nuevo objeto a la lista durante el programa.
            tipo = input("¿Es perro o gato? ").strip().lower()
            nombre = input("Nombre: ").strip()
            edad = pedir_edad()

            try:
                if tipo == "perro":
                    nueva_mascota = Perro(nombre, edad)
                elif tipo == "gato":
                    nueva_mascota = Gato(nombre, edad)
                else:
                    print("Tipo no válido. Escribe perro o gato.")
                    continue

                mascotas.append(nueva_mascota)
                print(nombre, "se agregó al catálogo.")

            except ValueError as error:
                print("No se pudo agregar la mascota:", error)

        elif opcion == "7":
            # CÁLCULOS SIMPLES: total, conteo y promedio.
            total = len(mascotas)
            suma_edades = 0
            cantidad_perros = 0
            cantidad_gatos = 0
            disponibles = 0

            for mascota in mascotas:
                suma_edades = suma_edades + mascota.get_edad()

                if mascota.tipo == "Perro":
                    cantidad_perros = cantidad_perros + 1
                elif mascota.tipo == "Gato":
                    cantidad_gatos = cantidad_gatos + 1

                if mascota.estado == "Disponible":
                    disponibles = disponibles + 1

            # Comprobamos que la lista no esté vacía antes de dividir.
            if total > 0:
                promedio = suma_edades / total
            else:
                promedio = 0

            print("\n--- REPORTE ---")
            print("Total de mascotas:", total)
            print("Perros:", cantidad_perros)
            print("Gatos:", cantidad_gatos)
            print("Disponibles para adopción:", disponibles)
            print("Promedio de edad:", round(promedio, 1), "años")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            # VALIDACIÓN: responde si la opción no existe.
            print("Opción no válida. Intenta de nuevo.")


# Esta línea inicia el programa.
iniciar_programa()