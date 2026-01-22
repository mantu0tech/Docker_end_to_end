# 🐳 Docker Compose – Complete Guide (SME Level)

This README explains **Docker Compose from scratch**, including:

* What Docker Compose is
* Why it is used
* Docker Compose file structure
* Explanation of **each keyword**
* Common Docker Compose commands
* Best practices

---

## 📌 What is Docker Compose?

**Docker Compose** is a tool used to **define and manage multi-container Docker applications** using a **single YAML file** (`docker-compose.yml`).

Instead of running multiple `docker run` commands, Docker Compose lets you **start everything with one command**.

---

## 🤔 Why Docker Compose?

Without Docker Compose:

```bash
docker run mysql
docker run backend
docker run frontend
```

With Docker Compose:

```bash
docker compose up
```

---

## ✅ Advantages of Docker Compose

* Manages **multiple containers**
* Easy service-to-service communication
* One command to start/stop everything
* Ideal for **local development & testing**
* Supports volumes, networks, environment variables

---

## 📄 What is `docker-compose.yml`?

It is a **YAML file** that defines:

* Services (containers)
* Images
* Ports
* Volumes
* Networks
* Environment variables

---

## 🧱 Basic Docker Compose File Structure

```yaml
version: "3.9"

services:
  app:
    image: myapp
    ports:
      - "5000:5000"

  db:
    image: mysql
```

---

## 🧪 Complete Example: Flask App + MySQL

```yaml
version: "3.9"

services:
  app:
    build: .
    container_name: flask_app
    ports:
      - "5000:5000"
    environment:
      MYSQL_HOST: db
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_DB: devops
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: mysql:8
    container_name: mysql_db
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: devops
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - app-network

volumes:
  mysql-data:

networks:
  app-network:
```

---

## 🔍 Explanation of Each Docker Compose Key

---

### 🔹 `version`

```yaml
version: "3.9"
```

* Defines the Compose file format
* Version 3+ is commonly used

---

### 🔹 `services`

```yaml
services:
```

* Defines all containers
* Each service = one container

---

### 🔹 `build`

```yaml
build: .
```

* Builds image using Dockerfile
* `.` = current directory

---

### 🔹 `image`

```yaml
image: mysql:8
```

* Uses a prebuilt image
* Can be from Docker Hub or private registry

---

### 🔹 `container_name`

```yaml
container_name: mysql_db
```

* Assigns a custom container name
* Optional

---

### 🔹 `ports`

```yaml
ports:
  - "5000:5000"
```

* Maps host port → container port
* Format: `HOST:CONTAINER`

---

### 🔹 `environment`

```yaml
environment:
  MYSQL_ROOT_PASSWORD: root
```

* Sets environment variables
* Used for app configuration

---

### 🔹 `depends_on`

```yaml
depends_on:
  - db
```

* Ensures container startup order
* Does NOT wait for service readiness

---

### 🔹 `volumes`

```yaml
volumes:
  - mysql-data:/var/lib/mysql
```

* Provides persistent storage
* Data survives container deletion

---

### 🔹 `networks`

```yaml
networks:
  - app-network
```

* Enables container-to-container communication
* Services can talk using service names

---

### 🔹 Named Volumes

```yaml
volumes:
  mysql-data:
```

* Managed by Docker
* Stored on host filesystem

---

### 🔹 Custom Networks

```yaml
networks:
  app-network:
```

* Isolated network for services
* Better security & DNS resolution

---

## ▶️ Docker Compose Commands (Most Important)

---

### 🔹 Start Services

```bash
docker compose up
```

---

### 🔹 Start in Detached Mode

```bash
docker compose up -d
```

✔ Runs containers in background

---

### 🔹 Stop Services

```bash
docker compose down
```

✔ Stops & removes containers
✔ Keeps volumes unless `-v` is used

---

### 🔹 Stop & Remove Volumes

```bash
docker compose down -v
```

⚠️ Deletes persistent data

---

### 🔹 View Running Services

```bash
docker compose ps
```

---

### 🔹 View Logs

```bash
docker compose logs
```

Specific service:

```bash
docker compose logs app
```

---

### 🔹 Rebuild Images

```bash
docker compose up --build
```

---

### 🔹 Restart Services

```bash
docker compose restart
```

---

## 🔁 Docker Compose vs Docker Run

| Feature          | docker run       | docker compose       |
| ---------------- | ---------------- | -------------------- |
| Multi containers | ❌ No             | ✅ Yes                |
| Networking       | Manual           | Automatic            |
| Volumes          | Manual           | Easy                 |
| Scaling          | Hard             | Easy                 |
| Best for         | Single container | Multi-container apps |

---

## ✅ Best Practices

✔ Use service names for communication
✔ Use volumes for databases
✔ Keep secrets in `.env` file
✔ Use `depends_on` wisely
✔ One service = one container

---

## 🎯 Interview One-Liners

* **Docker Compose** → Tool for running multi-container apps
* **Service** → One container
* **Volume** → Persistent data
* **Network** → Container communication
* **depends_on** → Startup order

---

## 📌 When to Use Docker Compose?

* Local development
* Testing environments
* POCs
* Small deployments

⚠️ Not recommended for large-scale production (use Kubernetes).

---

## 🚀 Final Summary

Docker Compose simplifies Docker by:

* Using a single YAML file
* Managing multiple services
* Providing easy networking & storage
* Reducing command complexity

---

Happy Composing 🐳
