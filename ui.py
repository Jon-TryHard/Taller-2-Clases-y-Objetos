from typing import List
from cuenta import Cuenta

class BancoUI:
    @staticmethod
    def mostrar_menu() -> str:
        print("\n" + "=" * 40)
        print("        SISTEMA DE GESTIÓN BANCARIA")
        print("=" * 40)
        print("1. Crear nueva cuenta")
        print("2. Depositar dinero (Aplica 19% retención)")
        print("3. Retirar dinero")
        print("4. Listar todas las cuentas de clientes")
        print("5. Salir")
        print("=" * 40)
        return input("Seleccione una opción: ").strip()

    @staticmethod
    def pedir_datos_nueva_cuenta():
        print("\n--- Registro de Nueva Cuenta ---")
        try:
            num = int(input("Ingrese el número de cuenta: "))
            doc = int(input("Ingrese documento de identidad: "))
            nombre = input("Ingrese nombre del cliente: ").strip()
            saldo = float(input("Ingrese saldo inicial: "))
            return num, doc, nombre, saldo
        except ValueError:
            print(">> Error: Formato de entrada no válido.")
            return None

    @staticmethod
    def listar_cuentas(cuentas: List[Cuenta]) -> None:
        print("\n--- Listado de Cuentas de Clientes ---")
        if not cuentas:
            print("No hay cuentas registradas en el sistema.")
            return
        for i, cuenta in enumerate(cuentas, 1):
            print(f"[{i}] {cuenta.mostrar_datos()}")

    @staticmethod
    def solicitar_numero_cuenta() -> int:
        try:
            return int(input("Ingrese el número de cuenta a operar: "))
        except ValueError:
            return -1

    @staticmethod
    def solicitar_monto(accion: str) -> float:
        try:
            return float(input(f"Ingrese monto a {accion}: "))
        except ValueError:
            return -1.0

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f">> {mensaje}")