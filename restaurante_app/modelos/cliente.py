
class Cliente:
    """Clase que representa un cliente del restaurante."""

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:

        self.identificacion = self.validar_identificacion(identificacion)
        self.nombre = self.validar_nombre(nombre)
        self.correo = self.validar_correo(correo)

    @staticmethod
    def validar_identificacion(identificacion: str) -> str:
        if not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")

        if not identificacion.isdigit():
            raise ValueError("La identificación debe contener solo números.")

        return identificacion

    @staticmethod
    def validar_nombre(nombre: str) -> str:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        return nombre.title()

    @staticmethod
    def validar_correo(correo: str) -> str:
        if not correo.strip():
            raise ValueError("El correo no puede estar vacío.")

        if "@" not in correo or "." not in correo:
            raise ValueError("Correo electrónico no válido.")

        return correo

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

