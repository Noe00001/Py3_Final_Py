# 📋 gestion-info

> Sistema de gestión de información por consola — CRUD limpio, persistencia en JSON y utilidades de datos integradas.

---

## ¿Qué es y por qué es útil?

**gestion-info** es una aplicación de línea de comandos desarrollada en Python que permite gestionar registros de información de forma estructurada. Cubre el ciclo completo de datos: creación, lectura, actualización y eliminación (CRUD), con persistencia local en JSON y soporte para generación de datos de prueba con Faker, análisis con Pandas y consumo de APIs externas con Requests.

Es útil para aprender arquitectura por capas, practicar separación de responsabilidades y tener una base sólida para proyectos de gestión de datos en consola.

---

## 🗂️ Estructura del proyecto

```
gestion-info/
│
├── assets/
│   ├── menu.py              
│   ├──Yum.py
│   ├──Yum1.py
│   ├──Yum2.py
│   ├──Yum3.py
│   ├──Yum4.py
│   ├──Yum5.py
│   └──Yum6.py
│
├── data/
│   └── records.json         
│
├── src/
│   ├── main.py              
│   ├── menu.py              
│   ├── service.py           
│   ├── file.py              
│   ├── validate.py          
│   └── integration.py       
│
├── tests/
│   └── test.py              
│
├── .gitignore
├── requirements.txt
└── README.md
```

**Capas de la arquitectura:**

| Capa | Archivo | Responsabilidad |
|---|---|---|
| Punto de entrada | `main.py` | Inicia la aplicación |
| UI / Consola | `menu.py` | Muestra menús e interacción |
| Lógica CRUD | `service.py` | Crear, leer, actualizar, eliminar |
| Persistencia | `file.py` | Leer y guardar en `records.json` |
| Validaciones | `validate.py` | Verificar datos del usuario |
| Integraciones | `integration.py` | Faker, Pandas, Requests |

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/Noe00001/Py3_Final_Py
cd gestion-info
```

### 2. Crea y activa un entorno virtual

```bash
# Crear
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS / Linux
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el proyecto

```bash
python src/main.py
```

---

## 🧪 Pruebas

El proyecto incluye una suite de pruebas unitarias en `tests/test.py` que cubre la creación, listado y eliminación de usuarios. Los tests usan mocking para simular entradas del usuario sin requerir interacción real con la consola.

### Pruebas cubiertas

| # | Función testeada | Descripción |
|---|---|---|
| 1 | `validate_user()` | Crea un usuario con inputs simulados y verifica todos sus campos |
| 2 | `list_records()` | Lista registros existentes y verifica que `print` sea invocado |
| 3 | `delete_record()` | Elimina un usuario por ID y verifica que la lista quede vacía |

### Ejecutar con `unittest` (sin dependencias extra)

Desde la raíz del proyecto:

```bash
python -m unittest tests/test.py -v
```

La flag `-v` activa el modo verbose para ver el nombre y resultado de cada test individualmente:

```
test_1_crear_usuario (tests.test.TestGestionInfo) ... ok
test_2_listar_usuarios (tests.test.TestGestionInfo) ... ok
test_3_eliminar_usuario (tests.test.TestGestionInfo) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.012s

OK
```

### Ejecutar con `pytest` (recomendado)

Instala pytest si no lo tienes:

```bash
pip install pytest
```

Luego, desde la raíz del proyecto:

```bash
# Ejecutar todos los tests
pytest tests/

# Con salida detallada
pytest tests/ -v

# Con resumen de cobertura por módulo
pytest tests/ -v --tb=short
```

Salida esperada con `-v`:

```
tests/test.py::TestGestionInfo::test_1_crear_usuario PASSED
tests/test.py::TestGestionInfo::test_2_listar_usuarios PASSED
tests/test.py::TestGestionInfo::test_3_eliminar_usuario PASSED

3 passed in 0.08s
```

### Criterios de aceptación de las pruebas

- ✅ Los 3 tests pasan sin errores.
- ✅ No hay lógica de negocio dentro del menú (`menu.py` solo llama a `service.py`).
- ✅ Las validaciones están centralizadas en `validate.py`, sin duplicación.
- ✅ Cada test resetea el estado global en `setUp()` para ser independiente.

---

## 🖥️ Uso

Al ejecutar el proyecto se muestra el menú principal en consola:

```
==================================
       GESTIÓN DE INFORMACIÓN
==================================
  [1] Ver todos los registros
  [2] Agregar nuevo registro
  [3] Actualizar registro
  [4] Eliminar registro
  [5] Generar datos de prueba
  [0] Salir
==================================
Selecciona una opción:
```

### Ejemplos de flujo

**Agregar un registro:**
```
Selecciona una opción: 2
Nombre: Juan Pérez
Email: juan@email.com
✅ Registro guardado correctamente.
```

**Generar datos de prueba con Faker:**
```
Selecciona una opción: 5
¿Cuántos registros deseas generar? 10
✅ 10 registros generados y guardados.
```

**Ver registros (con resumen Pandas):**
```
Selecciona una opción: 1
ID  | Nombre        | Email
----|---------------|------------------
1   | Juan Pérez    | juan@email.com
2   | Ana García    | ana@email.com
...
Total de registros: 2
```

---

## 👤 Créditos / Autores

| Rol | Nombre |
|---|---|
| Desarrollador principal | [@Noe00001](https://github.com/Noe00001) |

¿Quieres contribuir? Haz un fork del repositorio, crea una rama con tu mejora (`git checkout -b feature/mi-mejora`) y abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.

Puedes usar, copiar, modificar y distribuir el código libremente, siempre que incluyas el aviso de copyright original. No se ofrece ninguna garantía sobre el software.

```
MIT License © 2026 Noe00001
```

---

<div align="center">
  <sub>Construido con Python 🐍 · Faker · Pandas · Requests</sub>
</div>