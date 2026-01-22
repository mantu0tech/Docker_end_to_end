# Dockerfile: ADD vs CMD

This document explains the **ADD instruction**, **CMD instruction**, and their differences in Dockerfiles.

---

## 🔹 ADD Instruction

`ADD` is used to **copy files, directories, or remote URLs** into a Docker image.

### Syntax

```dockerfile
ADD <source> <destination>
```

### Features

* Copies local files
* Extracts `.tar` archives automatically
* Downloads files from URLs
* Runs at **image build time**

### Example

```dockerfile
ADD myapp.tar.gz /app
```

---

## 🔹 CMD Instruction

`CMD` defines the **default command** that runs when a container starts.

### Syntax

```dockerfile
CMD ["executable", "param1", "param2"]
```

### Features

* Runs at **container runtime**
* Can be overridden during `docker run`
* Only one CMD is effective

### Example

```dockerfile
CMD ["python", "app.py"]
```

---

## 🔸 ADD vs CMD Comparison

| Feature     | ADD            | CMD             |
| ----------- | -------------- | --------------- |
| Type        | File operation | Runtime command |
| Executed at | Build time     | Container start |
| Primary use | Copy files     | Run application |
| Overrides   | ❌ No           | ✅ Yes           |

---

## 🔸 ADD vs COPY (Best Practice)

| Feature      | COPY  | ADD               |
| ------------ | ----- | ----------------- |
| Predictable  | ✅ Yes | ❌ Less            |
| Remote URL   | ❌ No  | ✅ Yes             |
| Auto extract | ❌ No  | ✅ Yes             |
| Recommended  | ✅ Yes | ⚠️ Only if needed |

---

## ✅ Best Practices

* Prefer `COPY` over `ADD`
* Use `ADD` only for tar extraction or URLs
* Use `CMD` for default runtime commands
* Combine with `ENTRYPOINT` for production containers

---

## 🎯 Interview Tip

> *ADD copies files during build, CMD runs commands at container startup.*

---

Make sure Dockerfiles stay **simple, predictable, and secure**.
