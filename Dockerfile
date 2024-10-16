# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Get the PORT environment variable from Render (default to 8000)
ENV PORT=${PORT:-8000}

# Use a shell to run the command so it can expand environment variables
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}

