
# Tejidos Tayet
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

Plataforma web e-commerce diseñada para la venta de productos artesanales y tejidos hechos a mano, integrando gestión de pedidos personalizados y pasarela de pagos en línea.

---

## 🚀 Características Principales

* **🔐 Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión de usuarios (`Login` / `Register`).
* **🛍️ Catálogo de Productos:** Exposición visual interactiva de los artículos y tejidos disponibles.
* **✍️ Pedidos Personalizados:** Sección para que los clientes soliciten productos a la medida.
* **💳 Pasarela de Pago Integrada:** Procesamiento de pagos seguros con **Webpay Plus** (Transbank).
* **🔍 Buscador de Productos:** Funcionalidad de búsqueda rápida para los artículos del sitio.
* **📩 Formulario de Contacto:** Vía directa de comunicación entre el cliente y la tienda.
* **📱 Diseño Responsive:** Interfaz adaptada a dispositivos móviles, tablets y escritorio con Bootstrap.

---

## 🛠️ Tecnologías Utilizadas

### **Backend**
* **Python** — Lenguaje principal de programación.
* **Django** — Framework web de alto nivel para el desarrollo rápido y seguro.

### **Frontend**
* **HTML5 & CSS3** — Estructura y estilos personalizados.
* **Bootstrap 5** — Framework para el diseño responsivo y componentes UI.

### **Integraciones & Pasarelas**
* **Webpay Plus (Transbank)** — Integración de flujo de pago mediante SDK / API.

---

## ⚙️ Instalación y Configuración Local

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/simplementebolk/tienda.git
cd tienda
```

### 2. Crear el entorno virtual
```bash
# En Windows
python -m venv venv

# En macOS / Linux
python3 -m venv venv
```

### 3. Activar el entorno virtual
```bash
# En Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# En Windows (CMD)
venv\Scripts\activate.bat

# En macOS / Linux
source venv/bin/activate
```

### 4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 5. Aplicar las migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear Super Usuario(Administrador)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

### 8. Accede a la aplicación en tu navegador:
```bash
Sitio Web: http://127.0.0.1:8000/

Panel de Administración: http://127.0.0.1:8000/admin/
```

### 9. Configuración de Webpay Plus

Ejemplo de variables de configuración para el entorno de integración en Django (settings.py):

```bash
WEBPAY_COMMERCE_CODE = '11111111111111'
WEBPAY_API_KEY = '1111111111111111111111111111111'
WEBPAY_ENVIRONMENT = 'TEST'
```
