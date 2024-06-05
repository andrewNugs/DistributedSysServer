# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN pip install flask hashids requests

# Run server.py when the container launches
CMD ["python", "load_balancer.py"]
