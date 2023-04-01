# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy your Python script(s) into the container
COPY . /app

# Set the command to run your Python script(s)
CMD ["python", "your-script.py"]