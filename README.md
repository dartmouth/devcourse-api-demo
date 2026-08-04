# Campus‑Coffee Demo API
A tiny FastAPI project that showcases the **Router → Controller → Service → Model** architecture pattern, using SQLite + SQLModel.

> **Purpose:**  
> Use this repo for the *Session 1* presentation (walk‑through of the code) and then let participants build a different API (**Dartmouth Places**) in *Session 2* using the same structure.

---

## 📚 Table of Contents
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Running the Server](#running-the-server)
- [Testing the Endpoints (CLI)](#testing-the-endpoints-cli)
- [Optional: Enable Authentication & PATCH](#optional-enable-authentication--patch)
- [Project Structure Explained](#project-structure-explained)

---

## Prerequisites
- Python **3.10** or newer (the code uses the `|` union syntax).
- `git` (to clone the repo).
- A terminal / command prompt.
- UV installed

---

## Setup & Installation

```bash
# 1️ Clone the repo (or create the folder structure manually)
git clone https://github.com/your‑org/devcourse-api-demo.git
cd devcourse-api-demo

# 2️ (Recommended) Create a virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3️ Install dependencies
pip install -r requirements.txt

# 4 Run the server
uvicorn app.main:app --reload
```
