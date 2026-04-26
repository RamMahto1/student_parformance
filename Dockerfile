# Use stable base (important for ML)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy full project
COPY . .

# Expose Flask port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]