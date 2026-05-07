# =========================================================
# RedBlue Forensics
# Autor: David
# Herramienta: Hash Checker Forense
# Descripción: Calculadora de hashes para análisis forense
# Versión: 1.0
# =========================================================

import hashlib
import os
import sys


def calcular_hashes(ruta_archivo):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    try:
        with open(ruta_archivo, "rb") as archivo:
            while chunk := archivo.read(4096):
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)

        return {
            "MD5": md5.hexdigest(),
            "SHA1": sha1.hexdigest(),
            "SHA256": sha256.hexdigest()
        }

    except FileNotFoundError:
        print("\n[ERROR] Archivo no encontrado.")
        sys.exit(1)

    except Exception as error:
        print(f"\n[ERROR] {error}")
        sys.exit(1)


def mostrar_banner():
    print("=" * 60)
    print("RedBlue Forensics")
    print("Autor: David")
    print("Hash Checker Forense")
    print("=" * 60)


def main():
    mostrar_banner()

    if len(sys.argv) != 2:
        print("\nUso:")
        print("python hash_checker.py archivo")
        sys.exit(1)

    ruta_archivo = sys.argv[1]

    if not os.path.isfile(ruta_archivo):
        print("\n[ERROR] El archivo indicado no existe.")
        sys.exit(1)

    hashes = calcular_hashes(ruta_archivo)

    print(f"\nArchivo analizado: {ruta_archivo}\n")

    for tipo, valor in hashes.items():
        print(f"{tipo}: {valor}")


if __name__ == "__main__":
    main()