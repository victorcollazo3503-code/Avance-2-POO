# Avance 2: Herencia, Encapsulamiento y Polimorfismo
# Sistema de control de acceso para gimnasio

# Creacion de la clase base
class MiembroGimnasio:
    def __init__(self, nombre, tipo_membresia, enfoque_entrenamiento):
        self.nombre = nombre
        self.tipo_membresia = tipo_membresia
        self.enfoque_entrenamiento = enfoque_entrenamiento
        self.activa = True
        
        # Aplicacion de Encapsulamiento (atributo privado)
        self.__visitas_mes = 0 

    # Getters y Setters para proteger los datos
    def get_visitas_mes(self):
        return self.__visitas_mes

    def set_visitas_mes(self, cantidad):
        if cantidad >= 0:
            self.__visitas_mes = cantidad
        else:
            print("Error: Las visitas no pueden ser negativas.")

    # Metodos operativos
    def registrar_acceso(self):
        if self.activa:
            self.__visitas_mes += 1
            print(f"Acceso concedido a {self.nombre}. Total de visitas del mes: {self.__visitas_mes}")
        else:
            print(f"Acceso denegado. La membresia de {self.nombre} se encuentra inactiva.")
            
    def renovar_membresia(self):
        self.activa = True
        self.__visitas_mes = 0
        print(f"La membresia {self.tipo_membresia} de {self.nombre} fue renovada con exito.")
        
    def suspender_membresia(self):
        self.activa = False
        print(f"Alerta en el sistema: La membresia de {self.nombre} ha sido suspendida.")
        
    # Este metodo se va a sobrescribir despues
    def mostrar_info(self):
        estado = "Activa" if self.activa else "Inactiva"
        return f"Plan Basico - Miembro: {self.nombre} | Plan: {self.tipo_membresia} | Estado: {estado} | Visitas: {self.get_visitas_mes()}"


# Uso de super() y Herencia
class MiembroVIP(MiembroGimnasio):
    def __init__(self, nombre, enfoque_entrenamiento, entrenador_personal, creditos_spa):
        # Usamos super() para traer los datos de la clase padre
        super().__init__(nombre, "Membresia VIP", enfoque_entrenamiento)
        
        # Atributos exclusivos de la subclase
        self.entrenador_personal = entrenador_personal
        self.creditos_spa = creditos_spa

    def usar_spa(self):
        if self.creditos_spa > 0:
            self.creditos_spa -= 1
            print(f"{self.nombre} entro al SPA. Le quedan {self.creditos_spa} creditos disponibles.")
        else:
            print(f"{self.nombre} ya no tiene creditos para el SPA.")

    # Sobrescritura de metodos (Polimorfismo)
    def mostrar_info(self):
        estado = "Activa" if self.activa else "Inactiva"
        return f"Plan VIP - Miembro: {self.nombre} | Entrenador: {self.entrenador_personal} | Creditos SPA: {self.creditos_spa} | Estado: {estado} | Visitas: {self.get_visitas_mes()}"


# ==========================================
# Instanciacion y pruebas
# ==========================================

print("--- REGISTRO DE USUARIOS ---")
miembro_base = MiembroGimnasio("Armando", "Mensual", "Acondicionamiento general")
miembro_vip1 = MiembroVIP("Victor Collazo", "Hipertrofia muscular y fuerza", "Roberto", 5)
miembro_vip2 = MiembroVIP("Norma", "Clases grupales", "Ana", 2)

print("\n--- PROBANDO ACCESOS Y HERENCIA ---")
miembro_base.registrar_acceso()
miembro_vip1.registrar_acceso()
miembro_vip1.usar_spa()

print("\n--- PROBANDO ENCAPSULAMIENTO ---")
miembro_base.set_visitas_mes(4)
print(f"Las visitas de {miembro_base.nombre} se actualizaron a: {miembro_base.get_visitas_mes()} (usando el getter)")

print("\n--- PROBANDO POLIMORFISMO ---")
print(miembro_base.mostrar_info())
print(miembro_vip1.mostrar_info())
print(miembro_vip2.mostrar_info())