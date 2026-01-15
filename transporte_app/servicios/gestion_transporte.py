class GestionTransporte:
    """Servicio para gestionar las operaciones de los vehículos."""

    def realizar_mantenimiento(self, vehiculo):
        """Demostración de polimorfismo: acepta cualquier tipo de Vehiculo."""
        print(f"Iniciando mantenimiento para: {vehiculo.marca}")
        print(f"Acción: {vehiculo.describir_comportamiento()}")
        print("Mantenimiento completado con éxito.\n")