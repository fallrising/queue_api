# Base image
FROM registry.cn-shenzhen.aliyuncs.com/ckczgq/python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY queue_api.py .

# Expose the port
EXPOSE 8090

# Start the Flask application
CMD ["python", "queue_api.py"]

