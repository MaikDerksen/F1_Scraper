# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port if needed for services (if applicable)
# EXPOSE 5000  # Uncomment if your application needs to expose a port (e.g., Flask/Django)

# Command to run your Python script
CMD ["python", "main.py"]
