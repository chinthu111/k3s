# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY app.py .

# Install any needed packages
RUN pip install --no-cache-dir logging

# Run the application
CMD ["python", "app.py"]