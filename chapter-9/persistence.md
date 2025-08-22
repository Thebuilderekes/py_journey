 # Persistence

## ✅ Concept of Persistence in Python

**Persistence** in Python refers to **the ability to save data** or the **state of a program** so that it can be retrieved and used later, even after the program has ended. This is useful when you want to store user data, configurations, machine learning models, objects, or program state between executions.

In simpler terms:

> **Persistence = Saving and retrieving data across program runs.**

---

## 🧩 Topics, Modules, and Functions Related to Persistence in Python

Here’s a breakdown of the **main tools and concepts** for persistence in Python:

---

### 🔹 1. **File I/O (Text and Binary Files)**

#### ✅ Topics:

* Reading from and writing to files
* Working with binary data

#### ✅ Functions/Methods:

* `open()`, `read()`, `write()`, `close()`, `with open(...)`

#### ✅ Example:

```python
with open("data.txt", "w") as f:
    f.write("Hello, world!")
```

---

### 🔹 2. **Pickle Module** (Object Serialization)

Used to save **Python objects** (like lists, dicts, custom classes) in a file in binary format.

#### ✅ Module:

* `pickle`

#### ✅ Functions:

* `pickle.dump(obj, file)`
* `pickle.load(file)`

#### ✅ Example:

```python
import pickle

data = {'name': 'Alice', 'age': 30}

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
    loaded = pickle.load(f)
```

---

### 🔹 3. **JSON Module** (Text-based Serialization)

Used to serialize data in a format that is human-readable and language-independent.

#### ✅ Module:

* `json`

#### ✅ Functions:

* `json.dump(obj, file)`
* `json.load(file)`
* `json.dumps(obj)`
* `json.loads(str)`

#### ✅ Example:

```python
import json

data = {'name': 'Bob', 'age': 25}

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    loaded = json.load(f)
```

---

### 🔹 4. **Database Persistence (SQLite)**

For storing structured data persistently using a database.

#### ✅ Module:

* `sqlite3` (built-in)

#### ✅ Topics:

* CRUD operations
* SQL queries

#### ✅ Example:

```python
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
c.execute('INSERT INTO users (id, name) VALUES (?, ?)', (1, 'Alice'))

conn.commit()
conn.close()
```

---

### 🔹 5. **Shelve Module**

Combines features of `pickle` and `dbm`, allowing you to store Python objects in a **dictionary-like file**.

#### ✅ Module:

* `shelve`

#### ✅ Example:

```python
import shelve

with shelve.open('mydata') as db:
    db['x'] = [1, 2, 3, 4]

with shelve.open('mydata') as db:
    print(db['x'])
```

---

### 🔹 6. **Third-party Modules**

#### ✅ `joblib` (for large numpy arrays and machine learning models)

```python
from joblib import dump, load

dump(my_model, 'model.joblib')
model = load('model.joblib')
```

#### ✅ `sqlalchemy` (ORM for databases)

#### ✅ `h5py` or `PyTables` (for large data and scientific computing)

---

## 🗂 Summary Table

| Method    | Module    | Use Case                          |
| --------- | --------- | --------------------------------- |
| Text File | `open()`  | Simple data or logs               |
| Pickle    | `pickle`  | Python object serialization       |
| JSON      | `json`    | Cross-language readable data      |
| Shelve    | `shelve`  | Persistent dict-like storage      |
| SQLite    | `sqlite3` | Lightweight database              |
| Joblib    | `joblib`  | Efficient model and array storage |

---
