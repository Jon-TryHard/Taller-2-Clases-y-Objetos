class Cuenta:
    def __init__(self, numero_cuenta: int, documento_identidad: int, nombre: str, saldo: float = 0.0):
        # El número de cuenta no tiene método mutador (setter)
        self._numero_cuenta = int(numero_cuenta)
        self._documento_identidad = int(documento_identidad)
        self._nombre = str(nombre)
        self._saldo = float(saldo)

    # Getters
    @property
    def numero_cuenta(self) -> int:
        return self._numero_cuenta

    @property
    def documento_identidad(self) -> int:
        return self._documento_identidad

    @documento_identidad.setter
    def documento_identidad(self, nuevo_doc: int) -> None:
        self._documento_identidad = int(nuevo_doc)

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = str(nuevo_nombre)

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar_dinero(self, monto: float) -> bool:
        """Deposita dinero aplicando una retención del 19%."""
        if monto <= 0:
            return False
        retencion = monto * 0.19
        monto_neto = monto - retencion
        self._saldo += monto_neto
        return True

    def retirar_dinero(self, monto: float) -> bool:
        """Permite retirar dinero si existe saldo suficiente."""
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            return True
        return False

    def mostrar_datos(self) -> str:
        """Retorna una cadena con la información detallada de la cuenta."""
        return (
            f"No. Cuenta: {self._numero_cuenta} | "
            f"Doc. Identidad: {self._documento_identidad} | "
            f"Cliente: {self._nombre} | "
            f"Saldo Actual: ${self._saldo:,.2f}"
        )