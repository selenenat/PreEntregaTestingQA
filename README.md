# PreEntregaQA - Suite de Pruebas Automatizadas (SauceDemo)

Este proyecto contiene una suite de pruebas automatizadas de UI utilizando **Python**, **Selenium WebDriver** y **Pytest** para la aplicación web [SauceDemo](https://www.saucedemo.com/).

---

## 🛠️ Tecnologías y Herramientas Utilizadas

* **Lenguaje:** Python 3.14+
* **Framework de Testing:** `pytest`
* **Automatización Web:** `selenium`
* **Administrador de Drivers:** `webdriver-manager`

---

## 📁 Estructura del Proyecto

```text
PreEntregaQA/
├── tests/
│   └── test_saucedemo.py   # Script principal con los casos de prueba
├── utils/
│   └── helpers.py          # Funciones auxiliares / helpers
├── .venv/                  # Entorno virtual de Python
├── README.md               # Documentación del proyecto
```

---

## 🚀 Requisitos Previos e Instalación

### 1. Clonar o descargar el repositorio
Ubicarse en la carpeta raíz del proyecto:
```bash
cd PreEntregaQA
```

### 2. Crear y activar el entorno virtual
En macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install pytest selenium webdriver-manager
```

---

## 🧪 Casos de Prueba Incluidos

El archivo `tests/test_saucedemo.py` incluye el flujo completo e interconectado de pruebas utilizando una *fixture* con `scope="module"` para compartir la misma sesión del navegador:

1. **`test_01_login`**: Inicia sesión en la plataforma con credenciales válidas y verifica la redirección a `/inventory.html`.
2. **`test_02_verificar_inventario`**: Valida el título de la página web (`Swag Labs`) y el encabezado de sección (`Products`).
3. **`test_03_productos_visibles`**: Asegura que la lista de productos se despliegue en la interfaz.
4. **`test_04_validad_interfaz`**: Comprueba la presencia del menú hamburguesa y del filtro de ordenamiento de productos.
5. **`test_05_añadir_productos_al_carrito`**: Selecciona el primer producto e interactúa con el botón `Add to cart`.
6. **`test_06_verificar_contador_carrito`**: Verifica que la notificación del carrito incremente a `"1"`.
7. **`test_07_navegar_carrito`**: Presiona el icono del carrito y confirma la navegación hacia `/cart.html`.
8. **`test_08_comprobar_poducto_en_el_carrito`**: Valida que el producto agregado corresponda a `'Sauce Labs Backpack'`.

---

## ▶️ Ejecución de las Pruebas

Para ejecutar la suite completa de pruebas desde la terminal:

```bash
pytest
```

Para ver la ejecución detallada paso a paso en la terminal:

```bash
pytest -v
```