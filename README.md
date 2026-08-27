# Campus‑Coffee Demo API
A tiny FastAPI project that showcases the **Router → Controller → Service → Model** architecture pattern, using SQLite + SQLModel.

> **Purpose:**
> Use this repo for the *Session 1* presentation (walk‑through of the code) and then let participants build a different API (**Dartmouth Places**) in *Session 2* using the same structure.

---

## 📚 Table of Contents
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)

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
git clone -b api-skeleton git@github.com:dartmouth/devcourse-api-demo.git
cd devcourse-api-demo

# 2️ Initialize the environment and install dependencies
uv sync

# 3 Run the server
uv run fastapi dev
```
