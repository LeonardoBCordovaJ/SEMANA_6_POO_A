from .vehiculo import Vehiculo

class Moto(Vehiculo):
    """Clase Moto que hereda de Vehiculo (Pilar: Herencia)."""

    def describir_comportamiento(self) -> str:
        # Pilar: Polimorfismo (Implementación específica para Moto)
        return f"La moto {self.marca} {self.modelo} arranca usando el equilibrio del conductor."