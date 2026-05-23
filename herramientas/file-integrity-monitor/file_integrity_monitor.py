# =========================================================
# RedBlue Forensics
# Autor: David
# Herramienta: File Integrity Monitor
# Descripción: Monitor básico de integridad de archivos
# Versión: 1.0
# =========================================================

import hashlib
import os
import sys
import json
from datetime import datetime


BASELINE_FILE = "baseline_hashes.json"


def mostrar_banner():
    print("=" * 60)
    print("RedBlue Forensics")
    print("Autor: David")
    print("File Integrity Monitor")
    print("=" * 60)


def calcular_sha256(ruta_archivo):
    sha256 = hashlib.sha256()

    with open(ruta_archivo, "rb") as archivo:
        while chunk := archivo.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def obtener_archivos_directorio(ruta_directorio):
    archivos = []

    for raiz, _, nombres_archivos in os.walk(ruta_directorio):
        for nombre in nombres_archivos:
            ruta_completa = os.path.join(raiz, nombre)

            if os.path.isfile(ruta_completa):
                archivos.append(ruta_completa)

    return archivos


def crear_baseline(ruta_directorio):
    baseline = {
        "directorio": ruta_directorio,
        "fecha_creacion": datetime.now().isoformat(),
        "archivos": {}
    }

    archivos = obtener_archivos_directorio(ruta_directorio)

    for archivo in archivos:
        try:
            baseline["archivos"][archivo] = calcular_sha256(archivo)
        except Exception as error:
            print(f"[ERROR] No se pudo procesar {archivo}: {error}")

    with open(BASELINE_FILE, "w", encoding="utf-8") as salida:
        json.dump(baseline, salida, indent=4, ensure_ascii=False)

    print(f"\n[OK] Baseline creada correctamente.")
    print(f"[INFO] Archivo generado: {BASELINE_FILE}")


def verificar_integridad():
    if not os.path.exists(BASELINE_FILE):
        print("\n[ERROR] No existe baseline previa.")
        print("Primero ejecuta:")
        print("python file_integrity_monitor.py baseline carpeta")
        sys.exit(1)

    with open(BASELINE_FILE, "r", encoding="utf-8") as entrada:
        baseline = json.load(entrada)

    print(f"\nBaseline original: {baseline.get('fecha_creacion')}")
    print(f"Directorio analizado: {baseline.get('directorio')}\n")

    cambios_detectados = False

    for archivo, hash_original in baseline["archivos"].items():
        if not os.path.exists(archivo):
            print(f"[ELIMINADO] {archivo}")
            cambios_detectados = True
            continue

        hash_actual = calcular_sha256(archivo)

        if hash_actual != hash_original:
            print(f"[MODIFICADO] {archivo}")
            cambios_detectados = True

    archivos_actuales = set(obtener_archivos_directorio(baseline["directorio"]))
    archivos_originales = set(baseline["archivos"].keys())

    nuevos = archivos_actuales - archivos_originales

    for archivo in nuevos:
        print(f"[NUEVO] {archivo}")
        cambios_detectados = True

    if not cambios_detectados:
        print("[OK] No se detectaron cambios.")


def main():
    mostrar_banner()

    if len(sys.argv) < 2:
        print("\nUso:")
        print("python file_integrity_monitor.py baseline carpeta")
        print("python file_integrity_monitor.py check")
        sys.exit(1)

    accion = sys.argv[1].lower()

    if accion == "baseline":
        if len(sys.argv) != 3:
            print("\n[ERROR] Debes indicar una carpeta.")
            print("Ejemplo:")
            print("python file_integrity_monitor.py baseline carpeta_prueba")
            sys.exit(1)

        ruta_directorio = sys.argv[2]

        if not os.path.isdir(ruta_directorio):
            print("\n[ERROR] La ruta indicada no es una carpeta válida.")
            sys.exit(1)

        crear_baseline(ruta_directorio)

    elif accion == "check":
        verificar_integridad()

    else:
        print("\n[ERROR] Acción no reconocida.")
        print("Acciones válidas: baseline, check")
        sys.exit(1)


if __name__ == "__main__":
    main()