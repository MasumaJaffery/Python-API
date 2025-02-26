# Python-API

## 📌 Overview
This is a simple Python-based API built using Flask. It provides RESTful endpoints for managing data and can be extended with a database.

## ⚙️ Installation

### **1️⃣ Prerequisites**
Ensure you have Python installed. Check by running:
```bash
python --version
```
If not installed, download it from [Python.org](https://www.python.org/downloads/).

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/MasumaJaffery/Python-API
cd Python-API
```

### **3️⃣ Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Running the API

### **Start the Flask Server**
```bash
python app.py
```

The API will run at: **http://127.0.0.1:5000/**

## 📡 API Endpoints

| Method | Endpoint         | Description              |
|--------|----------------|--------------------------|
| **GET** | `/fruits`       | Get all fruits           |
| **GET** | `/fruits/<id>`  | Get a fruit by ID        |
| **POST** | `/fruits`      | Add a new fruit          |
| **PUT** | `/fruits/<id>`  | Update fruit by ID       |
| **DELETE** | `/fruits/<id>` | Delete fruit by ID      |

## 📝 Example Requests

### **Get All Fruits**
```bash
curl -X GET http://127.0.0.1:5000/fruits
```

### **Add a New Fruit**
```bash
curl -X POST http://127.0.0.1:5000/fruits -H "Content-Type: application/json" -d '{"name": "Mango", "color": "Yellow"}'
```

## 🛠 Deployment
To deploy the API, you can use **Gunicorn** for production:
```bash
pip install gunicorn
```
Run the API:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 👥 Contributors
- [Syeda Masuma Fatima](https://github.com/MasumaJaffery)

## 📜 License
This project is licensed under the MIT License.

