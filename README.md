🛒 Ecommerce Wildev
Plataforma de e‑commerce desarrollada en Flask con arquitectura modular, preparada para escalar y adaptarse a proyectos comerciales reales.
Incluye gestión de productos, carrito de compras, usuarios y una base sólida para futuras integraciones (pagos, panel admin, etc.).

📌 Características principales
✅ Arquitectura Flask con Blueprints

🛍️ Catálogo de productos

🛒 Carrito de compras funcional

👤 Gestión de usuarios (login / logout)

🧩 Templates con Jinja2

🎨 Frontend basado en HTML + CSS + Bootstrap

🔐 Preparado para integrar Flask-Login

⚙️ Configuración lista para entorno local y VPS

🧱 Estructura del proyecto

```text
Ecommerce-Wildev/
            │
            ├── app/
            │   ├── __init__.py          # Factory create_app()
            │   ├── routes/
            │   │   ├── shop.py          # Rutas de la tienda
            │   │   ├── cart.py          # Rutas del carrito
            │   │   └── auth.py          # Autenticación (opcional)
            │   │
            │   ├── templates/
            │   │   ├── base.html
            │   │   ├── shop/
            │   │   │   └── index.html
            │   │   └── cart/
            │   │       └── view.html
            │   │
            │   ├── static/
            │   │   ├── css/
            │   │   ├── js/
            │   │   └── images/
            │   │
            │   └── models/              # Modelos (futuro ORM)
            │
            ├── run.py                   # Punto de entrada
            ├── requirements.txt
            ├── .env.example
            ├── README.md
            └── .gitignore
```

🚀 Instalación y ejecución
1️⃣ Clonar el repositorio

```bash
git clone https://github.com/wildevsoluciones/Ecommerce-Wildev.git
cd Ecommerce-Wildev
```

2️⃣ Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows
```

3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

4️⃣ Variables de entorno
Crear un archivo .env (o usar .env.example):

```bash
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_aqui
```

5️⃣ Ejecutar la aplicación

```bash
flask run
```

🌐 Acceder a la aplicación

Abrir el navegador y navegar a:

```http://
http://127.0.0.1:5000
```

🔗 Rutas principales

| Ruta      | Descripción               |
| --------- | ------------------------- |
| `/`       | Página principal (tienda) |
| `/cart`   | Ver carrito               |
| `/login`  | Login de usuario          |
| `/logout` | Cerrar sesión             |

🛒 Carrito de compras
Gestión mediante sesión con funcionalidades para:

- Añadir productos al carrito
- Ver productos en el carrito
- Eliminar productos del carrito
- Actualizar cantidades

🔐 Autenticación
El proyecto está preparado para integrar:

- Registro de usuarios
- Login / Logout
- Panel de usuario

🧪 Testing (pendiente)
Sugerido para próximas versiones:

- Pruebas unitarias con pytest
- Pruebas de integración
- Cobertura de código

🌍 Deploy
Compatible con:

- VPS (DigitalOcean, Linode, etc.)
- Plataformas PaaS (Heroku, PythonAnywhere)
- Contenedores Docker (futuro)
- GitHub Actions para CI/CD (futuro)

📈 Próximas mejoras
🧾 Base de datos con SQLAlchemy

💳 Pasarela de pagos (MercadoPago / Stripe)

🧑‍💼 Panel administrador

📦 Gestión de stock

📊 Dashboard de ventas

📱 Diseño responsive mejorado

👨‍💻 Autor
Wildev Soluciones
Desarrollo de software y soluciones web a medida.

🔗 GitHub: https://github.com/wildevsoluciones
🌐 Sitio web: https://wildevshop.com.ar

📄 Licencia
Este proyecto es de uso privado/comercial.
Para uso o redistribución contactar al autor.
