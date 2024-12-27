# Use the official Python image from Docker Hub
FROM python:latest


# Set environment variable to prevent Python from buffering the output
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /backend
WORKDIR /backend

# Copy the requirements.txt file from the current directory to the working directory in the container
COPY requirements.txt .

# Install the Python dependencies from the requirements.txt file
RUN pip3 install -r requirements.txt

# Copy all the files from the current directory to the working directory in the container
COPY . . 

# Set the command to run when the container starts
CMD python manage.py runserver 0.0.0.0:8000