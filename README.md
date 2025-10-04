# 📦 API de Categorías

API REST construida con **Flask**, **SQLAlchemy** y **MySQL**.  
Base de datos en **Railway** y desplegada en **Render**.

---

## 🚀 Endpoints disponibles

### 🔹 Obtener todas las categorías
**GET** `/categorias`

📌 Ejemplo:
```bash
curl -X GET https://tu-api.onrender.com/categorias
```

📥 Respuesta:
```json
[
  {
    "id": 1,
    "nombre": "usb",
    "descripcion": ""
  },
  {
    "id": 2,
    "nombre": "Mouse",
    "descripcion": ""
  }
]
```

---

### 🔹 Obtener una categoría por ID
**GET** `/categorias/<id>`

📌 Ejemplo:
```bash
curl -X GET https://tu-api.onrender.com/categorias/1
```

📥 Respuesta:
```json
{
  "id": 1,
  "nombre": "usb",
  "descripcion": ""
}
```

---

### 🔹 Crear una nueva categoría
**POST** `/categorias`  
📌 Body (JSON):
```json
{
  "nombre": "Parlantes",
  "descripcion": "Dispositivos de sonido"
}
```

📌 Ejemplo:
```bash
curl -X POST https://tu-api.onrender.com/categorias   -H "Content-Type: application/json"   -d '{"nombre":"Parlantes","descripcion":"Dispositivos de sonido"}'
```

📥 Respuesta:
```json
{
  "id": 3,
  "nombre": "Parlantes",
  "descripcion": "Dispositivos de sonido"
}
```

---

### 🔹 Actualizar una categoría
**PUT** `/categorias/<id>`  
📌 Body (JSON):
```json
{
  "nom_cat": "Mouse Gamer",
  "descripcion": "Ratón con luces RGB"
}
```

📌 Ejemplo:
```bash
curl -X PUT https://tu-api.onrender.com/categorias/2   -H "Content-Type: application/json"   -d '{"nom_cat":"Mouse Gamer","descripcion":"Ratón con luces RGB"}'
```

📥 Respuesta:
```json
{
  "id": 2,
  "nombre": "Mouse Gamer",
  "descripcion": "Ratón con luces RGB"
}
```

---

### 🔹 Eliminar una categoría
**DELETE** `/categorias/<id>`

📌 Ejemplo:
```bash
curl -X DELETE https://tu-api.onrender.com/categorias/3
```

📥 Respuesta:
```json
{
  "mensaje": "Categoría eliminada correctamente"
}
```

---

## 🛠️ Tecnologías usadas
- **Flask** (framework web en Python)  
- **Flask SQLAlchemy** (ORM)  
- **PyMySQL** (driver MySQL)  
- **Gunicorn** (servidor de producción)  
- **Railway** (base de datos MySQL)  
- **Render** (hosting de la API)  

---

## 📂 Estructura del proyecto

```
api_categorias/
│── app.py              # Código principal Flask
│── requirements.txt    # Dependencias
│── Procfile            # Configuración Render
│── README.md           # Documentación
```

---

## ⚙️ Despliegue en Render

1. Subir repo a GitHub  
2. Conectar a Render  
3. Configurar:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`  
4. Agregar variable de entorno:
   - `SQLALCHEMY_DATABASE_URI` = `mysql+pymysql://root:XXXX@caboose.proxy.rlwy.net:43751/railway`

---

✅ ¡Listo! Tu API estará disponible en:  
```
https://tu-api.onrender.com
```
(reemplaza con tu URL real de Render).
