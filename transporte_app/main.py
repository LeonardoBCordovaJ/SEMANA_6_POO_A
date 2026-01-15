from modelos.auto import Auto
from modelos.moto import Moto
from servicios.gestion_transporte import GestionTransporte


def main():
    # Instanciación de objetos
    mi_auto = Auto("Toyota", "Corolla", 4)
    mi_moto = Moto("Yamaha", "MT-07")

    # Uso de encapsulación
    mi_auto.registrar_recorrido(150.5)

    # Servicio de gestión
    gestor = GestionTransporte()

    print("--- Demostración de Pilares POO ---")
    gestor.realizar_mantenimiento(mi_auto)
    gestor.realizar_mantenimiento(mi_moto)


if __name__ == "__main__":
    main()