from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que administra el restaurante."""

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []
  
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si el código no existe."""

        for item in self.productos:
            if item.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def registrar_bebida(self, bebida: Bebida) -> bool:
        """Registra una bebida utilizando el mismo método de productos."""
        return self.registrar_producto(bebida)
 
    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente si la identificación no existe."""

        for item in self.clientes:
            if item.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True

    def listar_productos(self) -> None:

        if not self.productos:
            print("\nNo existen productos registrados.")
            return

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            print(producto.mostrar_informacion())
    
    def listar_clientes(self) -> None:

        if not self.clientes:
            print("\nNo existen clientes registrados.")
            return

        print("\n========== CLIENTES ==========")

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())