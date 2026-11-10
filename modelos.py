# ==========================================
# CLASE AUXILIAR PARA COMPOSICIÓN
# ==========================================
class PlanEntrenamiento:
    def __init__(self, enfoque, dias_por_semana):
        self.enfoque = enfoque
        self.dias_por_semana = dias_por_semana

    def obtener_rutina(self):
        return f"Plan enfocado en {self.enfoque} ({self.dias_por_semana} días a la semana)."

# ==========================================
# CLASE BASE
# ==========================================
class MiembroGimnasio:
    def __init__(self, nombre, tipo_membresia, plan_entrenamiento):
        self.nombre = nombre
        self.tipo_membresia = tipo_membresia
        
        # COMPOSICIÓN: Un Miembro "tiene-un" PlanEntrenamiento (es un objeto, no un string)
        self.plan_entrenamiento = plan_entrenamiento
        
        self.activa = True
        # Aplicación de Encapsulamiento (atributo privado)
        self.__visitas_mes = 0 

    # Getters y Setters para proteger los datos
    def get_visitas_mes(self):
        return self.__visitas_mes

    def set_visitas_mes(self, cantidad):
        if cantidad >= 0:
            self.__visitas_mes = cantidad
        else:
            print("Error: Las visitas no pueden ser negativas.")

    # Métodos operativos
    def registrar_acceso(self):
        if self.activa:
            self.__visitas_mes += 1
            print(f"Acceso concedido a {self.nombre}. Total de visitas del mes: {self.__visitas_mes}")
        else:
            print(f"Acceso denegado. La membresía de {self.nombre} se encuentra inactiva.")
            
    def renovar_membresia(self):
        self.activa = True
        self.__visitas_mes = 0
        print(f"La membresía {self.tipo_membresia} de {self.nombre} fue renovada con éxito.")
        
    def suspender_membresia(self):
        self.activa = False
        print(f"Alerta en el sistema: La membresía de {self.nombre} ha sido suspendida.")
        
    # Este método se va a sobrescribir después
    def mostrar_info(self):
        estado = "Activa" if self.activa else "Inactiva"
        return f"Plan Básico - Miembro: {self.nombre} | Plan: {self.tipo_membresia} | Enfoque: {self.plan_entrenamiento.enfoque} | Estado: {estado} | Visitas: {self.get_visitas_mes()}"

# ==========================================
# SUBCLASE (Herencia)
# ==========================================
class MiembroVIP(MiembroGimnasio):
    def __init__(self, nombre, plan_entrenamiento, entrenador_personal, creditos_spa):
        # Usamos super() para traer los datos de la clase padre
        super().__init__(nombre, "Membresía VIP", plan_entrenamiento)
        
        # Atributos exclusivos de la subclase
        self.entrenador_personal = entrenador_personal
        self.creditos_spa = creditos_spa

    def usar_spa(self):
        if self.creditos_spa > 0:
            self.creditos_spa -= 1
            print(f"{self.nombre} entró al SPA. Le quedan {self.creditos_spa} créditos disponibles.")
        else:
            print(f"{self.nombre} ya no tiene créditos para el SPA.")

    # Sobrescritura de métodos (Polimorfismo)
    def mostrar_info(self):
        estado = "Activa" if self.activa else "Inactiva"
        return f"Plan VIP - Miembro: {self.nombre} | Entrenador: {self.entrenador_personal} | Créditos SPA: {self.creditos_spa} | Estado: {estado} | Visitas: {self.get_visitas_mes()}"