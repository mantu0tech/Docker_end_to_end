## 3️⃣ Why Do DevOps Engineers Use Docker Multi-Stage Builds?

Think of it like **manufacturing a product** 🏭

* **Stage 1 → Factory floor**

  * Heavy tools
  * Compilers
  * Build dependencies

* **Stage 2 → Final packaged product**

  * Only what is needed to *run*
  * No tools, no source code, no clutter

Docker **multi-stage builds** allow you to use **multiple `FROM` statements** in one Dockerfile and copy only the required output to the final image.

---

## 🔍 Single-Stage vs Multi-Stage Build

| Feature                    | Single-Stage Build | Multi-Stage Build    |
| -------------------------- | ------------------ | -------------------- |
| Image size                 | Large              | Small                |
| Build tools in final image | Yes                | ❌ No                 |
| Security                   | Lower              | ✅ Higher             |
| Attack surface             | Bigger             | Smaller              |
| Build caching              | Limited            | Better (layer reuse) |
| Production readiness       | Not optimal        | ✅ Best practice      |
| CI/CD friendly             | Less               | ✅ Highly suitable    |

---

## ✅ Why DevOps Engineers Prefer Multi-Stage Builds

* 🔒 **Improved security**

  * No compilers or package managers in production image
* 📦 **Smaller image size**

  * Faster pull & deploy
* 🚀 **Faster startup time**
* 🧹 **Cleaner images**
* 🔁 **Better CI/CD pipelines**
* ☁️ **Lower cloud cost** (less storage & bandwidth)

---

## 📌 When NOT to Use Multi-Stage Builds

* Very simple scripts
* Debug-only images
* Temporary development containers

In **production**, multi-stage builds are the **default best practice**.

---

## 🧪 Example: Docker Multi-Stage Build (Flask App)

### Scenario

* Build dependencies needed only during build
* Runtime image should be lightweight

---

### 🧾 Dockerfile (Multi-Stage)

```dockerfile
# -------------------------
# Stage 1: Build Stage
# -------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# -------------------------
# Stage 2: Runtime Stage
# -------------------------
FROM python:3.11-alpine

WORKDIR /app

# Copy only required dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## 🔍 What’s Happening Here?

* **Stage 1 (builder)**

  * Installs dependencies
  * Uses pip tools
* **Stage 2 (runtime)**

  * Copies only installed packages
  * No build tools included
  * Smaller & secure image

---

## 📊 Image Size Comparison (Real-World)

| Build Type                | Approx Image Size |
| ------------------------- | ----------------- |
| Single-stage Python image | ~900 MB           |
| Multi-stage Python image  | ~120–150 MB       |

---
