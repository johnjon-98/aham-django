
# 📘 Jon Fund API Documentation


## 🚀 First-Time Setup Guide

Follow these steps to set up and launch the Jon Fund API locally for the first time.


### 🛠️ Step-by-Step Setup

#### 1. Create and Activate Virtual Environment ✅
Set up a Python virtual environment to manage dependencies:
```bash
python -m venv .venv/
source .venv/bin/activate
```

#### 2. Install Dependencies ✅
Install all required packages from requirements.txt:
```bash
pip install -r requirements.txt
```

#### 3. Apply Database Migrations
Initialize the database schema with Django migrations:
```bash
python manage.py migrate
```

#### 4. Start the Development Server
Launch the server on your local machine:
```bash
python manage.py runserver
```

#### 5. Access the Interactive API Docs
Open your browser and navigate to the interactive documentation to explore and test the API: http://127.0.0.1:8000/docs/ \
![Screenshot of teh interactive documentation terminal.](/documentation.png)

#### 6. Perform systematic test
Run the following command to run written test cases:
```bash
python manage.py test fund
```
<br>
<br>

---
## 🧾 API Endpoints & Sample Data
---

### 🟢 Create a Fund  
**POST** `/api/fund_c/`  
Creates a new fund instance.

#### 📥 Sample Request Body
```json
{
    "name": "Fund 1",
    "manager": "Alice",
    "description": "A globally diversified equity investment fund.",
    "net_asset_value": 25000000,
    "performance": 8.4
}
```

#### 📤 Sample Response
```json
{
    "data": {
        "id": 1,
        "name": "Fund 1",
        "manager": "Alice",
        "description": "A globally diversified equity investment fund.",
        "net_asset_value": 25000000,
        "performance": 8.4
    },
    "message": "New Fund Created"
}
```

---

### 🔴 Delete a Fund  
**DELETE** `/api/fund_d/{id}`  
Deletes a fund by ID.

#### 🔗 Sample Path
```
/api/fund_d/1
```

#### 📤 Sample Response
```json
{
  "message": "Fund with ID 1 has been successfully deleted."
}
```

---

### 📃 List Funds  
**GET** `/api/fund_l/`  
Retrieves a list of all fund instances.

#### 📤 Sample Response
```json
[
    {
        "id": 1,
        "name": "Fund 1",
        "manager": "Alice",
        "created_date": "2025-04-20"
    },
    {
        "id": 2,
        "name": "Fund 2",
        "manager": "Ben",
        "created_date": "2025-04-20"
    },
    {
        "id": 3,
        "name": "Fund 3",
        "manager": "Calvin",
        "created_date": "2025-04-20"
    },
]
```

---

### 🔍 Retrieve a Fund Details
**GET** `/api/fund_r/{id}`  
Retrieves a single fund details by ID.

#### 🔗 Sample Path
```
/api/fund_r/2
```

#### 📤 Sample Response
```json
{
  "id": 2,
  "name": "Fund 2",
  "manager": "Ben",
  "description": "Focuses on growth opportunities in emerging markets.",
  "net_asset_value": 18000000,
  "created_date": "2025-04-20",
  "performance": 10.2
}
```

---

### 📝 Update a Fund  
**PUT** `/api/fund_u/{id}`  
Fully updates a fund by ID.

#### 🔗 Sample Path
```
/api/fund_u/1
```

#### 📥 Sample Request Body
```json
{
  "name": "EM Fund",
  "manager": "Alice",
  "description": "Updated description for the emerging markets fund.",
  "net_asset_value": 20000000,
  "performance": 11.0
}
```

#### 📤 Sample Response
```json
{
  "id": 1,
  "name": "EM Fund",
  "manager": "Alicia",
  "description": "Updated description for the emerging markets fund.",
  "net_asset_value": 20000000,
  "performance": 11.0
}
```

---

### ✏️ Partial Update a Fund  
**PATCH** `/api/fund_u/{id}`  
Partially updates a fund by ID.

#### 🔗 Sample Path
```
/api/fund_u/1
```

#### 📥 Sample Request Body
```json
{
  "performance": 10.2
}
```

#### 📤 Sample Response
```json
{
    "data": {
        "performance": 10.2
    },
    "message": "Fund with ID 1 has been successfully updated"
}
```
