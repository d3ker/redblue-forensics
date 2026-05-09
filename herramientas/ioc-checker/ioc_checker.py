# =========================================================
# RedBlue Forensics
# Autor: David
# Herramienta: IOC Checker
# Descripción: Clasificador básico de Indicadores de Compromiso
# Versión: 1.0
# =========================================================

import re
import sys


def mostrar_banner():
    print("=" * 60)
    print("RedBlue Forensics")
    print("Autor: David")
    print("IOC Checker")
    print("=" * 60)


def detectar_ioc(valor):
    patrones = {
        "IPv4": r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",
        "MD5": r"^[a-fA-F0-9]{32}$",
        "SHA1": r"^[a-fA-F0-9]{40}$",
        "SHA256": r"^[a-fA-F0-9]{64}$",
        "URL": r"^https?://[^\s/$.?#].[^\s]*$",
        "Dominio": r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$"
    }

    for tipo, patron in patrones.items():
        if re.match(patron, valor):
            return tipo

    return "Desconocido"


def main():
    mostrar_banner()

    if len(sys.argv) != 2:
        print("\nUso:")
        print("python ioc_checker.py indicador")
        print("\nEjemplos:")
        print("python ioc_checker.py 8.8.8.8")
        print("python ioc_checker.py ejemplo.com")
        print("python ioc_checker.py https://ejemplo.com/login")
        sys.exit(1)

    indicador = sys.argv[1].strip()
    tipo = detectar_ioc(indicador)

    print(f"\nIndicador analizado: {indicador}")
    print(f"Tipo detectado: {tipo}")


if __name__ == "__main__":
    main()