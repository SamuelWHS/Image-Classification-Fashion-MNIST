# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the Python dependencies file into the container
COPY requirements.txt .

# Upgrade pip to the latest version for better compatibility
RUN pip install --upgrade pip

# Install all required Python packages with an increased timeout for large packages
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Install system-level dependencies needed for image processing (e.g., Pillow)
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev

# Copy the app code and model files
COPY app.py .
COPY trained_model/ ./trained_model/

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
