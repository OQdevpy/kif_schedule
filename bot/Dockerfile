
# Use the official Python 3.10 image as the base
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot source code to the working directory
COPY . .

# Set the entrypoint command to run the bot
# CMD ["python", "app.py"]