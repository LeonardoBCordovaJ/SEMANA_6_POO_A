# Gestión de Vehículos - Semana 06
# Aplicativo de Gestión de Transporte - Semana 06

## Descripción
Este programa simula la gestión de diferentes tipos de vehículos, aplicando los cuatro pilares de la Programación Orientada a Objetos (POO).

## Pilares de la POO Implementados
1. **Abstracción**: Se utiliza la clase base `Vehiculo` como una clase abstracta (ABC) para definir métodos que todas las subclases deben tener.
2. **Herencia**: Las clases `Auto` y `Moto` heredan atributos y métodos de la clase `Vehiculo`.
3. **Encapsulación**: El atributo `_kilometraje` está protegido para evitar acceso directo, utilizando métodos para su modificación.
4. **Polimorfismo**: El método `describir_comportamiento` es sobrescrito en cada clase hija para realizar acciones diferentes según el tipo de objeto.

## Estructura del Proyecto
- `modelos/`: Contiene las definiciones de las clases (entidades).
- `servicios/`: Contiene la lógica de negocio y operaciones del sistema.
- `main.py`: Archivo principal para ejecutar y testear el aplicativo.

## Autor
Leonardo Benjamin Cordova Jaramillo