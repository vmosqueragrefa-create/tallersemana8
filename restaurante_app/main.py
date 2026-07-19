from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def pedir_producto() -> tuple[str, str, str, float]:
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))
    except ValueError:
        raise ValueError("El precio debe ser un número válido.")

    return codigo, nombre, categoria, precio


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar Producto ---")

    try:
        producto = Producto(*pedir_producto())

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Error: el código ya existe.")

    except ValueError as error:
        print(f"Error: {error}")


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\n--- Registrar Bebida ---")

    try:
        codigo, nombre, categoria, precio = pedir_producto()
        tamano = input("Tamaño: ")

        bebida = Bebida(
            codigo,
            nombre,
            categoria,
            precio,
            tamano
        )

        if restaurante.registrar_bebida(bebida):
            print("Bebida registrada correctamente.")
        else:
            print("Error: el código ya existe.")

    except ValueError as error:
        print(f"Error: {error}")


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\n--- Registrar Cliente ---")

    try:
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        cliente = Cliente(
            identificacion,
            nombre,
            correo
        )

        if restaurante.registrar_cliente(cliente):
            print("Cliente registrado correctamente.")
        else:
            print("Error: la identificación ya existe.")

    except ValueError as error:
        print(f"Error: {error}")


def main() -> None:
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            registrar_bebida(restaurante)

        elif opcion == "3":
            registrar_cliente(restaurante)

        elif opcion == "4":
            restaurante.listar_productos()

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()