# Dockerfile

# Use a specific Python base image for stability and smaller size
FROM python:3.11-slim-buster

# Set environment variables for non-interactive commands
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first to leverage Docker layer caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
# Also install netcat for the entrypoint's wait-for-db check
RUN apt-get update && apt-get install -y netcat-traditional && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    rm -rf /var/lib/apt/lists/* # Clean up apt cache

# Copy the rest of your Django project
COPY . /app

RUN python manage.py collectstatic --noinput

# Copy the entrypoint script into the container and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entrypoint to your script. This will always run first.
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Set the default command for the entrypoint script.
# This command will be executed by 'exec "$@"' inside entrypoint.sh
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "qs_world_ranking.wsgi:application"]

EXPOSE 8000