# 📰 Journal Information System – REST API

The Journal Information System is a Django-based RESTful API that provides endpoints for efficiently and structurally managing scientific journal data. This project uses the Django REST Framework, and API documentation is available through Swagger and Redoc.

---

## 🚀 Key Features
- Authentication and user management  
- CRUD operations for journal information  
- Relations with institutions, countries, and currencies  
- API documentation (Swagger, Redoc, OpenAPI)

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/tarokeitaro/sij-backend.git
cd sij-backend
```

### 2. Create a Virtual Environment
```bash
python -m venv venv 
```

Activate the Virtual Environment:
```bash
source venv/bin/activate # Linux/macOS
```
```bash
venv\Scripts\activate # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables  
Create a `.env` file in the root directory based on the example file:
```bash
cd sij
cp .env.example .env
```
Then adjust the environment values accordingly.

---

## ⚙️ Important Settings in `settings.py`
```conf
CORS_ALLOWED_ORIGINS = [
    "http://0.0.0.0:8000",
] 
CSRF_TRUSTED_ORIGINS = [
    'http://0.0.0.0:8000',
]
```
Make sure these settings are enabled during development so the frontend can securely access the API.

---

## 🧪 Running the Server
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```

---

## 📚 API Documentation  
Access the API documentation at the following endpoints:

- **OpenAPI schema (raw)**: [`/api/schema/`](http://localhost:8000/api/schema/)
- **Swagger UI**: [`/api/schema/swagger-ui/`](http://localhost:8000/api/schema/swagger-ui/)
- **Redoc**: [`/api/schema/redoc/`](http://localhost:8000/api/schema/redoc/)

---

## ✅ TODO
- [ ] User Rating
- [ ] User Comments
- [ ] Publisher Account  
- [ ] Publisher verification by admin

---

## 📬 Contact  
If you have any questions or would like to contribute, feel free to create an [issue](https://github.com/tarokeitaro/sij-backend/issues) or contact the project maintainer.