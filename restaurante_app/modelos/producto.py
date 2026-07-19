class Producto:
    """Clase base que representa un producto del restaurante."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> None:

        self.codigo = self.validar_codigo(codigo)
        self.nombre = self.validar_nombre(nombre)
        self.categoria = self.validar_categoria(categoria)
        self.precio = self.validar_precio(precio)

    @staticmethod
    def validar_codigo(codigo: str) -> str:
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        return codigo.upper()

    @staticmethod
    def validar_nombre(nombre: str) -> str:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return nombre.title()

    @staticmethod
    def validar_categoria(categoria: str) -> str:
        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        return categoria.title()

    @staticmethod
    def validar_precio(precio: float) -> float:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return precio

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )
