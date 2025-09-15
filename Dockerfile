# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend and frontend
COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Expose port
EXPOSE 5000

# Start the Flask app
CMD ["python", "/app/backend/app.py"]
