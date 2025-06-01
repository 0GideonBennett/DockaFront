# DockaFront ( Front-End Dockerizer)
A Python script that auto-Dockerizes static front-end apps (HTML, CSS, JS) using web servers like nginx:alpine. Designed to streamline Dockerfile generation, build, and container run steps through interactive prompts. Ideal for fast local testing or lightweight deployment.


---

## 🚀 Features

- Automatically generates a Dockerfile based on user input
- Supports popular static web server images
- Builds and runs the Docker container immediately
- Prompts user to stop/remove the container after deployment
- CLI-based, lightweight, and beginner-friendly

---

## 📦 Prerequisites

- **Docker Desktop** must be installed and actively running
- Your front-end project must:
  - Contain an `index.html` file
  - Be in the **same directory** as this script inside a folder (e.g., `./frontend`)
- Only tested with `nginx:alpine` (although designed for `php:apache` and `node` as well)

---

## 🧰 How to Use

1. Place this script in the same directory as your front-end folder (e.g., `./frontend`)
2. Run the script:
   ```bash
   python dockafront.py

### 📋 Follow the Prompts to:

- Choose a web server  
- Enter working directory for server (e.g., `/usr/share/nginx/html`)  
- Provide path to front-end folder (e.g., `./frontend`)  
- Specify exposed port (e.g., `80`)  
- Enter the CMD array (e.g., `["nginx", "-g", "daemon off;"]`)  

After successful build and run, visit:  
http://localhost:8080

Then follow script prompts to optionally stop and remove the container.


Then follow the script prompts to optionally stop and remove the container.

---

## 🛠 Known Issues & Solutions

### ❌ Issue: Port 8080 already in use  
**Cause:** Another container or local service is using the port.  
**Fix:**
docker ps        # to find running containers
docker stop <container_id>
docker rm <container_id>  # if needed


### ❌ Issue: CMD not found (e.g., [nginx, -g, daemon off;])
**Cause:** CMD was written in single quotes or not as valid JSON array.
**Fix:** Ensure CMD is passed as:

["nginx", "-g", "daemon off;"]
Script now auto-formats this using json.dumps() for correctness.

### ❌ Issue: Container name already in use
**Cause:** You're trying to reuse a container name that already exists.
**Fix:**

docker rm your-app-container
Or modify the script to use a unique container name.

### ❌ Issue: Blank screen on localhost
**Cause:** index.html file not found or improperly copied.
**Fix:**

Ensure your front-end directory has index.html directly inside (not nested)
Force rebuild if needed:

docker build --no-cache -t your-app .

## ⚠️ Professional Disclaimers
Script is designed for use with nginx:alpine, php:apache, and node, but was only tested with nginx:alpine.

Ensure Docker is running before starting the script.

Your front-end code must be inside the same directory as the script.

## 🌱 Future Improvements
Automatically check if port 8080 is in use before running

Auto-generate default CMDs for selected web servers

Allow persistent naming or versioning of containers

Add argparse support for advanced CLI usage

## 🙌 Author
Built by Gideon Bennett 






