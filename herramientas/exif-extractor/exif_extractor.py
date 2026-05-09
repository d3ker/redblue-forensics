# =========================================================
# RedBlue Forensics
# Autor: David
# Herramienta: EXIF Extractor
# Descripción: Extractor de metadatos EXIF para análisis forense
# Versión: 1.0
# =========================================================

import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def mostrar_banner():
    print("=" * 60)
    print("RedBlue Forensics")
    print("Autor: David")
    print("EXIF Extractor")
    print("=" * 60)


def obtener_datos_exif(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        exif_data = imagen.getexif()

        if not exif_data:
            print("\n[INFO] La imagen no contiene metadatos EXIF.")
            return

        print(f"\nImagen analizada: {ruta_imagen}\n")

        for tag_id, valor in exif_data.items():
            etiqueta = TAGS.get(tag_id, tag_id)
            print(f"{etiqueta}: {valor}")

    except FileNotFoundError:
        print("\n[ERROR] Archivo no encontrado.")
        sys.exit(1)

    except Exception as error:
        print(f"\n[ERROR] {error}")
        sys.exit(1)


def main():
    mostrar_banner()

    if len(sys.argv) != 2:
        print("\nUso:")
        print("python exif_extractor.py imagen.jpg")
        sys.exit(1)

    ruta_imagen = sys.argv[1]
    obtener_datos_exif(ruta_imagen)


if __name__ == "__main__":
    main()