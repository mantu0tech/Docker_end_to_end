# Docker Networking & Docker Volumes

This document explains **Docker network types**, **Docker Swarm basics**, and **how to use Docker volumes for persistent data**, using a **MySQL + Flask application** example.

---

## 🐳 Docker Network Types

Docker provides **7 types of networks**:

### 1. Host Network

* Removes network isolation.
* Container shares the **host’s network stack**.
* **High performance**, but **less secure**.
* **Linux-only**.

```
--network host
```

---

### 2. Bridge Network (Default)

* Default network for standalone containers.
* Containers get a **private internal IP**.
* Containers on the same bridge can communicate.
* External access requires **port mapping**.

```
--network bridge
```

---

### 3. User-Defined Bridge (Custom Bridge)

* Recommended over default bridge.
* Automatic **DNS-based container name resolution**.
* Better isolation and control.

```
docker network create mynet
```

---

### 4. None Network

* Completely **isolated container**.
* No external or internal network access.

```
--network none
```

---

### 5. Macvlan Network

* Container gets its **own MAC address**.
* Appears as a physical device on the network.
* Used mainly in **Docker Swarm** or legacy systems.

---

### 6. IPvlan Network

* Similar to Macvlan but shares MAC address.
* Better performance and simpler routing.

---

### 7. Overlay Network

* Used for **multi-host container communication**.
* Requires **Docker Swarm**.
* Enables containers on different hosts to communicate.

---

## 🚢 Docker Swarm (Brief Overview)

* Docker Swarm is Docker’s **native orchestration tool**.
* Used to manage **multiple Docker hosts**.
* Supports **overlay networks**, scaling, and load balancing.

⚠️ Today, **Kubernetes** is the industry standard, so Docker Swarm is **less commonly used**, but still good for learning fundamentals.

---

## 🌐 Docker Network Commands

List networks:

```bash
docker network ls
```

Create a custom bridge network:

```bash
docker network create mynet -d bridge
```

---

## 🛠 Application Setup (MySQL + Flask App)

### Step 1: Run MySQL Container

```bash
docker run -d \
--name mysql \
--network mynet \
-e MYSQL_ROOT_PASSWORD=root \
mysql
```

### Step 2: Access MySQL

```bash
docker exec -it mysql mysql -u root -p
```

Create database:

```sql
CREATE DATABASE devops;
SHOW DATABASES;
```

---

### Step 3: Build Application Image

```bash
docker build -t mgs-app .
```

---

### Step 4: Run Flask Application

```bash
docker run -d \
--name app \
--network mynet \
-p 5000:5000 \
-e MYSQL_HOST=mysql \
-e MYSQL_USER=root \
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_DB=devops \
mgs-app
```

✅ Application is now running successfully.

---

## 💾 Problem: Data Loss After Container Deletion

If you stop and remove the MySQL container:

```bash
docker stop mysql
docker rm mysql
```

All database data is **lost** because containers are **ephemeral**.

---

## 📦 Solution: Docker Volumes (Persistent Storage)

### Step 1: List Volumes

```bash
docker volume ls
```

### Step 2: Create Volume

```bash
docker volume create mydata
```

### Step 3: Inspect Volume

```bash
docker inspect mydata
```

This shows where Docker stores volume data on the host.

---

### Step 4: Recreate MySQL with Volume

```bash
docker run -d \
--name mysql \
--network mynet \
-v mydata:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=root \
mysql
```

📌 `/var/lib/mysql` is where MySQL stores its data.

---

### Step 5: Restart Application (If Needed)

```bash
docker restart app
```

---

## ✅ Result

* MySQL data is now **persistent**
* Even if the MySQL container is deleted and recreated
* Data remains stored in the Docker volume

---

## 🧠 Key Takeaways

* **Docker Networks** enable container communication
* **User-defined bridge networks** are best for single-host apps
* **Docker Volumes** persist data beyond container lifecycle
* **Docker Swarm** enables multi-host networking but is mostly replaced by Kubernetes

---

## 📌 Summary

| Feature         | Purpose                      |
| --------------- | ---------------------------- |
| Docker Network  | Container communication      |
| Docker Volume   | Persistent data storage      |
| Bridge Network  | Default container networking |
| Overlay Network | Multi-host networking        |
| Docker Swarm    | Container orchestration      |

---

🎯 **This setup is production-like and interview-ready.**
