FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Make the start script executable
RUN chmod +x /app/start.sh

# Set environment variables for Hugging Face
ENV BACKEND_URL=http://127.0.0.1:8000

# Hugging Face Spaces expects the app to be on port 7860
EXPOSE 7860

# Start both services using the shell script
CMD ["/bin/bash", "start.sh"]
