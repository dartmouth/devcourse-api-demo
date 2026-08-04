# Campus-Coffee API — Demo Commands

A walkthrough of every endpoint using `curl`.
Pipe to `python -m json.tool` for pretty-printed JSON (works anywhere Python does — no extra tools needed).

> **Before you start:** make sure the server is running:
> ```bash
> uvicorn app.main:app --reload
> ```
> The API lives at `http://127.0.0.1:8000`. Interactive docs: <http://127.0.0.1:8000/docs>

---

## 1. Health check

Confirms the server is up before touching any real endpoints.

```bash
# Simple liveness check — returns {"status": "ok"}
curl -s http://127.0.0.1:8000/health | python -m json.tool

# Create an Espresso — note the "id" in the response
curl -i -X POST http://127.0.0.1:8000/coffee/ \
     -H "Content-Type: application/json" \
     -d '{"name":"Espresso","price":2.5}'

# Add a couple more so the list/delete demos are interesting
curl -s -X POST http://127.0.0.1:8000/coffee/ \
     -H "Content-Type: application/json" \
     -d '{"name":"Latte","price":4.0}' | python -m json.tool

curl -s -X POST http://127.0.0.1:8000/coffee/ \
     -H "Content-Type: application/json" \
     -d '{"name":"Cold Brew","price":3.75}' | python -m json.tool

# Fetch the full menu
curl -s http://127.0.0.1:8000/coffee/ | python -m json.tool

# Fetch the coffee with id = 2
curl -s http://127.0.0.1:8000/coffee/2 | python -m json.tool

# Delete the coffee with id = 1
curl -i -X DELETE http://127.0.0.1:8000/coffee/1

# Confirm it's gone — id 1 should no longer appear in the list
curl -s http://127.0.0.1:8000/coffee/ | python -m json.tool

# Deleting it again returns 404 — it no longer exists
curl -i -X DELETE http://127.0.0.1:8000/coffee/1

# Negative price — returns 422 Unprocessable Entity with details
curl -i -X POST http://127.0.0.1:8000/coffee/ \
     -H "Content-Type: application/json" \
     -d '{"name":"Broken","price":-5}'