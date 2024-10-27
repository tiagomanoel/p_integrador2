FROM python:3.12-alpine3.20
LABEL maintainer="tiago.g.manoel@proton.me"

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Enable immediate output from Python (no buffering)
ENV PYTHONUNBUFFERED 1

# Copy application and script directories into the container
COPY djangoapp /djangoapp
COPY scripts /scripts
COPY request /scripts/request

# Set the working directory
WORKDIR /djangoapp

# Expose port 8000 for Django application
EXPOSE 8000

# Install necessary packages and set up the environment
RUN apk update && apk add --no-cache dcron bash sudo \
    && echo "0 */3 * * * /venv/bin/python3 /scripts/request/request_api.py" | crontab - \
    && mkdir -p /var/log/cron \
    && touch /var/log/cron/cron.log \
    && python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    addgroup duser wheel && \
    echo "duser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 777 /data/web/static && \
    chmod -R 777 /data/web/media && \
    chmod -R 777 /scripts && \
    chmod -R +x /scripts && \
    chmod +x /scripts/request/request_api.py && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# Add script and virtual environment bin directories to PATH
ENV PATH="/scripts:/venv/bin:$PATH"

# Switch to non-root user
USER duser

# Execute the command script
CMD ["commands.sh"]
