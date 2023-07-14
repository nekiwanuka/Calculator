# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
