# Hash Checker Forense

Herramienta desarrollada por **David – RedBlue Forensics** para el cálculo de hashes criptográficos en procesos de análisis forense digital.

---

# Descripción

Esta herramienta permite calcular hashes:

- MD5
- SHA1
- SHA256

de cualquier archivo indicado por el usuario.

Su finalidad es verificar la integridad de evidencias digitales durante procesos de:

- Informática forense
- DFIR
- Respuesta ante incidentes
- Validación de archivos
- Análisis técnico

---

# Características

- Cálculo de múltiples hashes
- Lectura eficiente de archivos grandes
- Manejo de errores
- Código limpio y documentado
- Compatible con Windows, Linux y macOS

---

# Estructura del proyecto

```text
hash-checker/
├── README.md
└── hash_checker.py
```

---

# Uso

## Ejecución básica

```bash
python hash_checker.py archivo.txt
```

---

# Ejemplo

```bash
python hash_checker.py evidencia.zip
```

---

# Resultado esperado

```text
============================================================
RedBlue Forensics
Autor: David
Hash Checker Forense
============================================================

Archivo analizado: evidencia.zip

MD5:     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SHA1:    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SHA256:  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# Tecnologías utilizadas

- Python 3
- hashlib
- os
- sys

---

# Autor

David  
Perito Judicial Informático  
RedBlue Forensics

---

# Aviso legal

Esta herramienta ha sido desarrollada exclusivamente con fines educativos, defensivos y de análisis autorizado.

El uso indebido de esta herramienta es responsabilidad exclusiva del usuario.