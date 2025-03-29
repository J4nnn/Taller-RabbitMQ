# Use the official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "producer:app", "--host", "0.0.0.0", "--port", "8000"]