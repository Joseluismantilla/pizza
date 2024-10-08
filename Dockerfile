# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pizza_ordering.wsgi:application"]

