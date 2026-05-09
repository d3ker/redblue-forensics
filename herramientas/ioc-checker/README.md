\# IOC Checker



Herramienta desarrollada por \*\*David – RedBlue Forensics\*\* para la clasificación básica de Indicadores de Compromiso.



\---



\# Descripción



IOC Checker permite identificar el tipo de indicador introducido:



\- Dirección IPv4

\- Dominio

\- URL

\- Hash MD5

\- Hash SHA1

\- Hash SHA256



\---



\# Uso



```bash

python ioc\_checker.py 8.8.8.8

```



\---



\# Ejemplos



```bash

python ioc\_checker.py ejemplo.com

python ioc\_checker.py https://ejemplo.com/login

python ioc\_checker.py 44d88612fea8a8f36de82e1278abb02f

```



\---



\# Resultado esperado



```text

============================================================

RedBlue Forensics

Autor: David

IOC Checker

============================================================



Indicador analizado: 8.8.8.8

Tipo detectado: IPv4

```



\---



\# Autor



David  

Perito Judicial Informático  

RedBlue Forensics



\---



\# Aviso legal



Herramienta desarrollada exclusivamente para análisis defensivo, investigación autorizada y formación técnica.



El uso indebido es responsabilidad exclusiva del usuario.

