# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install newspaper3k textblob

# Set an environment variable to prevent buffering of stdout/stderr
ENV PYTHONUNBUFFERED=1

# Install the nltk data
RUN python -m nltk.downloader punkt

# Run the Python script when the container starts
CMD ["python", "main.py"]
