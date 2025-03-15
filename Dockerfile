# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app will run on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0

# Define the command to run your app (this will start the Flask server)
CMD ["flask", "run"]