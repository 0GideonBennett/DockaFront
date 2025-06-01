#Script 2 - dockerizes a static frontend webapp  ( html,css, js)

import subprocess # allows us to run commands that we typically only run in our cli
import json

#Get user imput for all docker components needed (FROM, WORKDIR, COPY , EXPOSE, CMD)
print("Web-server Options: 'node', 'nginx:alpine', 'php:apache'")
webserver = input("Please Enter The Webserver You Want To Use:  ")
webserver_dir = input("Please Enter The Webserver DIR You Want To Use (i.e. For nginx:alpine it would be:\n/usr/share/nginx/html):  ")
frontend_loca = input("Please Enter The Location Of Your Frontend Code (i.e. ./frontend):  ")
expose = input("Please Enter The Expose Port Assignment (i.e. 443):  ")
cmd = input("""Please enter the CMD you would like: (i.e. ["nginx", "-g", "daemon off;"]): """)

#Webserver WORKDIR Variables 
#node = "/app"
#nginx_alpine = "" 
#php_apache = "/var/www/html"


# Create a docker file using the users input and then save it to their system
dock_file_content = f"""
        #Details what which webserver/base image this docker image will be built upon (think a template for our template).
        FROM {webserver}

        # Set the working directory
        WORKDIR {webserver_dir}

        # Copy the frontend folder contents to the webserver directory.
        COPY {frontend_loca} {webserver_dir}

        # The tells details what port the container will be on.
        EXPOSE {expose}

        CMD {json.dumps(parsed_cmd)}



        """
with open("Dockerfile", "w") as df:   # creating the docker file and assinging it to a var
    df.write(dock_file_content.strip())  # saving the docker content we made previously  to the docker file and strip just cleans the file up (e.g. removes whitespace)

# Build the Docker Image
subprocess.run(["docker", "build", "-t", "your-app", "."],check=True ) # here we are building the image and check=True is for error handling
# Run the Container
subprocess.run(["docker", "run", "-d", "-p", f"8080:{expose}" "--name", "your-app-container", "your-app"],check=True ) # here we are building the image and check=True is for error handling
# Provide them the http://localhost:8080 link so they can view it 

print("Your app is live and running. Go to this link to view it: http://localhost:8080  ")
# Ask them if they wish to stop the container  

choice1 = input("Do you wish to stop the container? (Enter: Y or N): ")

if choice1 == "Y":
    subprocess.run(["docker", "stop", "your-app-container"], check=True)
    # Ask them if they wish to remove the container  

    choice2 = input("Do you wish to remove the container? (Enter: Y or N): ")

    if choice2 == "Y":
        subprocess.run(["docker", "rm", "your-app-container"], check=True)
    else:
        print("Have a good day ;)")
  
else:
     print("Have a good day ;)")





