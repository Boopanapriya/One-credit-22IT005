# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy necessary files
COPY personal-api.py .

# Install Flask
RUN pip install flask

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "personal-api.py"]


