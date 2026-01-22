# 📘 Dockerfile – Complete Guide (DevOps Ready)

This README explains **Dockerfile basics to advanced concepts**, including **Docker images**, **how to build & run containers**, and **all Dockerfile instructions** with examples.

---

## 🐳 What is Docker?

Docker is a **containerization platform** that allows applications to run in **isolated environments** called containers.

* Lightweight
* Portable
* Consistent across environments

---

## 📄 What is a Dockerfile?

A **Dockerfile** is a **text file** that contains instructions to build a Docker image.

📌 It defines:

* Base OS
* Dependencies
* Application code
* Startup command

👉 Dockerfile is the **blueprint**, Docker image is the **product**, Docker container is the **running instance**.

---

## 🖼 What is a Docker Image?

A **Docker image** is a **read-only template** created from a Dockerfile.

* Contains application + runtime + dependencies
* Used to create containers
* Stored locally or in registries (Docker Hub, ECR, GCR)

### List images

```bash
docker images
```

---

## 📦 What is a Docker Container?

A **container** is a **running instance of an image**.

```bash
docker run myimage
```

---

## 🏗 How to Build a Docker Image

```bash
docker build -t myapp .
```

* `-t myapp` → image name
* `.` → current directory (Dockerfile location)

---

## ▶️ How to Run a Docker Container

```bash
docker run myapp
```

With port mapping:

```bash
docker run -p 5000:5000 myapp
```

Detached mode:

```bash
docker run -d myapp
```

---

## 🧱 Dockerfile Instructions (Complete List)

---

### 1️⃣ FROM

Defines the base image.

```dockerfile
FROM python:3.11
```

📌 Mandatory (except scratch images)

---

### 2️⃣ WORKDIR

Sets the working directory.

```dockerfile
WORKDIR /app
```

---

### 3️⃣ COPY

Copies files from host to image.

```dockerfile
COPY . /app
```

✅ Preferred over ADD

---

### 4️⃣ ADD

Like COPY, but with extra features.

```dockerfile
ADD app.tar.gz /app
```

Features:

* Auto-extract `.tar`
* Download URLs

⚠️ Use only if needed

---

### 5️⃣ RUN

Executes commands **at build time**.

```dockerfile
RUN pip install flask
```

Creates image layers.

---

### 6️⃣ ENV

Sets environment variables.

```dockerfile
ENV APP_ENV=production
```

---

### 7️⃣ EXPOSE

Documents the port used by the app.

```dockerfile
EXPOSE 5000
```

📌 Does NOT publish the port automatically.

---

### 8️⃣ CMD

Defines the **default runtime command**.

```dockerfile
CMD ["python", "app.py"]
```

🔹 Can be overridden during `docker run`

---

### 9️⃣ ENTRYPOINT

Defines a **fixed executable**.

```dockerfile
ENTRYPOINT ["python", "app.py"]
```

🔹 Arguments are appended, not replaced

---

### 🔥 CMD vs ENTRYPOINT (Very Important)

#### Dockerfile

```dockerfile
CMD ["python", "app.py"]
```

Behavior:

```bash
docker run myapp              # python app.py
docker run myapp other.py     # python other.py
```

➡ CMD is **overridden**

---

#### Dockerfile

```dockerfile
ENTRYPOINT ["python", "app.py"]
```

Behavior:

```bash
docker run myapp              # python app.py
docker run myapp other.py     # python app.py other.py
```

➡ ENTRYPOINT is **fixed**

---

#### Override ENTRYPOINT

```bash
docker run --entrypoint python myapp other.py
```

Result:

```bash
python other.py
```

---

### 🔟 VOLUME

Creates a mount point for persistent data.

```dockerfile
VOLUME /data
```

---

### 1️⃣1️⃣ USER

Runs container as a non-root user.

```dockerfile
USER appuser
```

🔒 Improves security

---

### 1️⃣2️⃣ ARG

Build-time variables.

```dockerfile
ARG VERSION=1.0
```

---

### 1️⃣3️⃣ LABEL

Adds metadata.

```dockerfile
LABEL maintainer="devops@example.com"
```

---

## 🧪 Sample Dockerfile (Best Practice)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## ✅ Dockerfile Best Practices

* Use **multi-stage builds**
* Prefer `COPY` over `ADD`
* Use `.dockerignore`
* Keep images small
* Avoid running as root
* Use `ENTRYPOINT + CMD` for flexibility

---

## 🎯 Interview One-Liners

* **Dockerfile** → Blueprint to build images
* **Image** → Read-only template
* **Container** → Running instance
* **CMD** → Default runtime command (overridable)
* **ENTRYPOINT** → Fixed executable
* **RUN** → Build-time command

---

## 📌 Summary Table

| Component        | Purpose              |
| ---------------- | -------------------- |
| Dockerfile       | Image definition     |
| Docker Image     | App + dependencies   |
| Docker Container | Running app          |
| CMD              | Default command      |
| ENTRYPOINT       | Fixed command        |
| RUN              | Build-time execution |

---

## 🚀 Final Note

This README covers **everything required for Docker fundamentals**, **DevOps interviews**, and **real-world usage**.

---

Happy Dockering 🐳
