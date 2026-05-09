\# EXIF Extractor



Herramienta desarrollada por \*\*David – RedBlue Forensics\*\* para la extracción de metadatos EXIF en imágenes digitales.



\---



\# Descripción



Esta herramienta permite analizar imágenes y extraer información EXIF útil en procesos de:



\- Informática forense

\- DFIR

\- Investigación digital

\- Análisis OSINT

\- Verificación de imágenes



\---



\# Información extraída



Dependiendo de la imagen:



\- Fecha de captura

\- Modelo de cámara

\- Fabricante

\- Software utilizado

\- Resolución

\- Coordenadas GPS

\- Metadata adicional



\---



\# Características



\- Extracción automática de metadatos

\- Compatible con imágenes JPG/JPEG

\- Manejo de errores

\- Código limpio y documentado

\- Compatible con Windows, Linux y macOS



\---



\# Estructura del proyecto



```text

exif-extractor/

├── README.md

└── exif\_extractor.py

```



\---



\# Uso



\## Ejecución básica



```bash

python exif\_extractor.py imagen.jpg

```



\---



\# Ejemplo



```bash

python exif\_extractor.py evidencia.jpg

```



\---



\# Resultado esperado



```text

============================================================

RedBlue Forensics

Autor: David

EXIF Extractor

============================================================



Imagen analizada: evidencia.jpg



Make: Canon

Model: EOS

DateTime: 2025:01:01 10:20:00

Software: Adobe Photoshop

```



\---



\# Dependencias



Instalar Pillow:



```bash

pip install pillow

```



\---



\# Tecnologías utilizadas



\- Python 3

\- Pillow (PIL)

\- EXIF Metadata



\---



\# Autor



David  

Perito Judicial Informático  

RedBlue Forensics



\---



\# Aviso legal



Herramienta desarrollada exclusivamente para:

\- investigación autorizada,

\- análisis defensivo,

\- informática forense,

\- fines educativos.



El uso indebido es responsabilidad exclusiva del usuario.

