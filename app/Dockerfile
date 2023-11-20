# Replace with your base image, tipically "python:3.12"
FROM python:3.12-alpine

# External file needed for program to execute, will be avaliable here
VOLUME [ "/opt/app/input" ]
# Put your output here
VOLUME [ "/opt/app/output" ]

# It is recomended to use "/app" as directory to run your program from
WORKDIR /app

# Copy files from local repo, replace with specific files if needed
COPY . .

# Repalce with your actual command
CMD [ "python", "main.py"]