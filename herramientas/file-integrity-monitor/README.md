\# File Integrity Monitor



Herramienta desarrollada por \*\*David – RedBlue Forensics\*\* para monitorizar cambios en archivos y verificar integridad mediante hashes SHA256.



\---



\## Descripción



File Integrity Monitor permite:



\- Detectar modificaciones en archivos

\- Identificar archivos eliminados

\- Detectar nuevos archivos

\- Verificar integridad mediante SHA256

\- Mantener una baseline de referencia



\---



\## Funcionalidades



\- Creación de baseline

\- Verificación de integridad

\- Detección de cambios

\- Detección de archivos nuevos

\- Detección de archivos eliminados

\- Soporte recursivo de directorios



\---



\## Estructura del proyecto



```text

file-integrity-monitor/

├── README.md

├── file\_integrity\_monitor.py

└── baseline\_hashes.json

```



\---



\## Uso



\### Crear baseline



```bash

python file\_integrity\_monitor.py baseline carpeta\_prueba

```



\---



\### Verificar integridad



```bash

python file\_integrity\_monitor.py check

```



\---



\## Ejemplo de resultado



```text

\[MODIFICADO] carpeta\_prueba/test.txt

\[NUEVO] carpeta\_prueba/nuevo.txt

\[ELIMINADO] carpeta\_prueba/viejo.txt

```



\---



\## Tecnologías utilizadas



\- Python 3

\- SHA256

\- JSON

\- Monitorización de integridad



\---



\## Aplicaciones DFIR



\- Detección de manipulación

\- Validación de integridad

\- Monitorización defensiva

\- Control de evidencias

\- Respuesta a incidentes



\---



\## Autor



David  

Perito Judicial Informático  

RedBlue Forensics



\---



\## Aviso legal



Herramienta desarrollada exclusivamente para:

\- investigación autorizada,

\- análisis defensivo,

\- informática forense,

\- entornos educativos y de laboratorio.

