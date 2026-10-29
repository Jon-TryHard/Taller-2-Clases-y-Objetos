from typing import List, Optional
from cuenta import Cuenta
from ui import BancoUI

def buscar_cuenta(cuentas: List[Cuenta], numero_cuenta: int) -> Optional[Cuenta]:
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta
    return None

def main():
    # Lista para almacenar todas las cuentas creadas (cuenta Clientes)
    cuenta_clientes: List[Cuenta] = []

    while True:
        opcion = BancoUI.mostrar_menu()

        if opcion == "1":
            datos = BancoUI.pedir_datos_nueva_cuenta()
            if datos:
                num, doc, nombre, saldo = datos
                if buscar_cuenta(cuenta_clientes, num):
                    BancoUI.mostrar_mensaje("Error: Ya existe una cuenta con ese número.")
                else:
                    nueva_cuenta = Cuenta(num, doc, nombre, saldo)
                    cuenta_clientes.append(nueva_cuenta)
                    BancoUI.mostrar_mensaje("Cuenta registrada exitosamente.")

        elif opcion == "2":
            num = BancoUI.solicitar_numero_cuenta()
            cuenta = buscar_cuenta(cuenta_clientes, num)
            if cuenta:
                monto = BancoUI.solicitar_monto("depositar")
                if cuenta.depositar_dinero(monto):
                    BancoUI.mostrar_mensaje(
                        f"Depósito realizado. Nuevo saldo tras 19% de retención: ${cuenta.saldo:,.2f}"
                    )
                else:
                    BancoUI.mostrar_mensaje("Error: El monto a depositar debe ser mayor a 0.")
            else:
                BancoUI.mostrar_mensaje("Cuenta no encontrada.")

        elif opcion == "3":
            num = BancoUI.solicitar_numero_cuenta()
            cuenta = buscar_cuenta(cuenta_clientes, num)
            if cuenta:
                monto = BancoUI.solicitar_monto("retirar")
                if cuenta.retirar_dinero(monto):
                    BancoUI.mostrar_mensaje(f"Retiro exitoso. Saldo restante: ${cuenta.saldo:,.2f}")
                else:
                    BancoUI.mostrar_mensaje("Error: Fondos insuficientes o monto no válido.")
            else:
                BancoUI.mostrar_mensaje("Cuenta no encontrada.")

        elif opcion == "4":
            BancoUI.listar_cuentas(cuenta_clientes)

        elif opcion == "5":
            BancoUI.mostrar_mensaje("Saliendo del sistema...")
            break

        else:
            BancoUI.mostrar_mensaje("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()