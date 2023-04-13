# Use a smaller base image
FROM python:3.11-slim AS build

RUN apt-get update && apt-get install -y build-essential

# Install required system packages
RUN apt-get update && apt-get install -y postgresql-client libpq-dev

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install packages and clean up cache
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the installed packages from the build stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /app /app

# Expose the port
EXPOSE 8000

# Define environment variable
ENV NAME portfolio_env

# Run your application when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
