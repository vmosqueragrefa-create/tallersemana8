# Restaurante App

## Estudiante

Victor Eduardo Mosquera Grefa

## Descripción

Restaurante App es un sistema desarrollado en Python utilizando Programación Orientada a Objetos. Permite registrar productos, bebidas y clientes mediante un menú interactivo en consola. El proyecto está organizado de forma modular para facilitar su mantenimiento y reutilización.

## Estructura del proyecto

restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md

## Responsabilidad de las clases

**Producto:** representa un producto del restaurante. 
**Bebida:** hereda de Producto y agrega el atributo `tamano`
**Cliente:** representa la información de un cliente.
**Restaurante:** administra el registro y listado de productos y clientes.
**main.py:** muestra el menú, solicita datos al usuario y llama a los métodos del servicio.

## Relación entre Producto y Bebida

La clase **Bebida** hereda de **Producto**, por lo que puede utilizarse como un producto más dentro del sistema. Esto permite aplicar herencia y polimorfismo utilizando una sola lista de productos.

## Principios SOLID aplicados

**SRP:** cada clase tiene una única responsabilidad.
 **OCP:** el sistema puede ampliarse con nuevos tipos de productos sin modificar la lógica principal.
 **LSP:** una bebida puede utilizarse como un producto sin afectar el funcionamiento del programa.

## Ejecución

Desde la carpeta `restaurante_app`, ejecutar:

python main.py

## Reflexión

La aplicación de los principios SOLID permite desarrollar programas más organizados, fáciles de mantener y preparados para incorporar nuevas funcionalidades mediante el uso de herencia y polimorfismo.
