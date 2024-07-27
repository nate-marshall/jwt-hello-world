# Use the official Python image as the base image
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a directory for the app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# # Create a non-root user and group
# RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# # Change ownership of the /app directory to the non-root user
# RUN chown -R appuser:appgroup /app

# # Switch to the non-root user
# USER appuser

# Expose the port that the Flask app runs on
EXPOSE 5000

# Run the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
