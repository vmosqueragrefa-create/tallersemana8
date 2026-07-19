from modelos.producto import Producto


class Bebida(Producto):
    """Clase que representa una bebida del restaurante."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = self.validar_tamano(tamano)

    @staticmethod
    def validar_tamano(tamano: str) -> str:
        if not tamano.strip():
            raise ValueError("El tamaño no puede estar vacío.")
        return tamano

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Tamaño: {self.tamano} | "
            f"Precio: ${self.precio:.2f}"
        )


