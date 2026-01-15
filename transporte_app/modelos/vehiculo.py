from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """
    Clase Abstracta Vehiculo (Pilar: Abstracción).
    Define la estructura base que todos los vehículos deben tener.
    """
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        # Pilar: Encapsulación (Atributo protegido con _)
        self._kilometraje = 0

    @abstractmethod
    def describir_comportamiento(self) -> str:
        """Método abstracto que obliga a las hijas a implementar su comportamiento."""
        pass

    def registrar_recorrido(self, km: float):
        """Método para modificar el atributo encapsulado."""
        if km > 0:
            self._kilometraje += km