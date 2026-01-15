from .vehiculo import Vehiculo


class Auto(Vehiculo):
    """Clase Auto que hereda de Vehiculo (Pilar: Herencia)."""

    def __init__(self, marca: str, modelo: str, puertas: int):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir_comportamiento(self) -> str:
        # Pilar: Polimorfismo (Implementación específica para Auto)
        return f"El auto {self.marca} enciende el motor y verifica las {self.puertas} puertas."