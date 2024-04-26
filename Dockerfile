# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and the text file into the container at /app
COPY stop.py paragraphs.txt /app/

# Install any dependencies required by your Python script
# For example, if your script requires NLTK, you can install it using pip
RUN pip install nltk

# Download NLTK data (if required)
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

# Command to run your Python script when the container starts
CMD ["python", "stop.py"]
