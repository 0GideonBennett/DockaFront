# Script: Dockerize a static frontend web app (HTML, CSS, JS)

import subprocess  # allows us to run CLI commands from Python
import ast         # safely evaluates string inputs (like CMD)
import json
# Get user input for all Docker components
print("Web-server Options: 'node', 'nginx:alpine', 'php:apache'")
webserver = input("Please Enter the Webserver You Want to Use: ")
webserver_dir = input("Please Enter the Webserver WORKDIR (i.e., /usr/share/nginx/html): ")
frontend_loca = input("Please Enter the Location of Your Frontend Code (e.g., ./frontend): ")
expose = input("Please Enter the Port to EXPOSE (i.e., 443): ")
cmd_input = input("""Please Enter the CMD (i.e., ["nginx", "-g", "daemon off;"]): """)


# Safely evaluate CMD input as list
try:
    parsed_cmd = ast.literal_eval(cmd_input)
    if not isinstance(parsed_cmd, list):
        raise ValueError
except Exception:
    print("❌ Invalid CMD format. Use a list like: [\"nginx\", \"-g\", \"daemon off;\"]")
    exit()

# Create Dockerfile content (no indentation)
dock_file_content = f"""
# Details which base image to use
FROM {webserver}

# Set the working directory
WORKDIR {webserver_dir}

# Copy the frontend files into the container
COPY {frontend_loca} {webserver_dir}

# Set the container's port
EXPOSE {expose}

# Start the server
CMD {json.dumps(parsed_cmd)}
"""

# Write the Dockerfile
with open("Dockerfile", "w") as df:
    df.write(dock_file_content.strip())

# Build the Docker image
subprocess.run(["docker", "build", "-t", "your-app", "."], check=True)

# Run the container
subprocess.run(["docker", "run", "-d", "-p", f"8080:{expose}", "--name", "your-app-container", "your-app"], check=True)

# Notify user
print("\n✅ Your app is live and running!")
print("🌐 Visit: http://localhost:8080")

# Ask if they want to stop the container
choice1 = input("\nDo you wish to stop the container? (Enter: Y or N): ")

if choice1.upper() == "Y":
    subprocess.run(["docker", "stop", "your-app-container"], check=True)

    # Ask if they want to remove the container
    choice2 = input("Do you wish to remove the container? (Enter: Y or N): ")

    if choice2.upper() == "Y":
        subprocess.run(["docker", "rm", "your-app-container"], check=True)
        print("Container removed. Have a good day! 🙂")
    else:
        print("Container stopped. You can restart it anytime.")
else:
    print("👍 Container is still running. Have a good day!")
