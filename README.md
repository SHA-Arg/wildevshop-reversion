# 🛒 WildevShop

**WildevShop** es una aplicación web de e‑commerce desarrollada con **Flask**, pensada como base sólida para una tienda online moderna.  
El proyecto está estructurado con **Blueprints**, preparado para escalar y para ser desplegado en un **VPS con Linux**.

---

## 🚀 Características principales

- Arquitectura Flask con `create_app`
- Uso de Blueprints (`shop`, `cart`, etc.)
- Renderizado con Jinja2
- Estructura lista para e‑commerce
- Preparado para despliegue en VPS
- Código organizado y mantenible

---

## 🧱 Estructura del proyecto

```text
wildevshop/
        │
        ├── app/
        │ ├── init.py # create_app y registro de blueprints
        │ ├── routes/
        │ │ ├── shop.py # Rutas de la tienda
        │ │ └── cart.py # Rutas del carrito
        │ ├── templates/
        │ │ ├── base.html # Template base
        │ │ └── shop/
        │ │ └── index.html # Home / productos
        │ └── static/
        │ ├── css/
        │ └── js/
        │
        ├── run.py # Punto de entrada de la app
        ├── requirements.txt # Dependencias
        └── README.md

```

---

## ⚙️ Requisitos

- Python **3.10+**
- pip
- Entorno Linux / VPS recomendado para producción

---

## 📦 Instalación local

1. Clonar el repositorio:

```bash
git clone https://github.com/wildevsoluciones/wildevshop.git

cd wildevshop

```

2. Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
flask run
```

# La app estará disponible en:

http://127.0.0.1:5000
🌐 Despliegue en VPS (resumen)

El proyecto está preparado para:

Nginx + Gunicorn

Deploy manual o automático desde GitHub

Uso de variables de entorno
(La configuración específica depende del servidor)

🛠 Tecnologías utilizadas

Python

Flask

Jinja2

HTML5 / CSS3

Git & GitHub

Linux VPS

📌 Próximos pasos (Roadmap)

🔐 Autenticación de usuarios

🛍️ Carrito persistente

💳 Integración de pagos

📦 Gestión de productos desde admin

📊 Panel de administración

👤 Autor
Desarrollado por Wildev Soluciones
📧 Contacto: wildevsoluciones@gmail.com
🌐 GitHub: https://github.com/wildevsoluciones

📄 Licencia
Este proyecto se distribuye bajo licencia MIT.
Libre para uso, modificación y distribución.

---
