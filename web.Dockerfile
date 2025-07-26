# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /app

# Install GDAL dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    curl \
    cron \
    && rm -rf /var/lib/apt/lists/*


ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install Python dependencies with Poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

# Copy the current directory contents into the container at /app/

COPY . /app/

RUN chmod +x ./entrypoint_web.sh
#RUN git update-index --chmod=+x ./run_tests.sh
#RUN git update-index --chmod=+x ./entrypoint_web.sh
CMD ["bash", "./entrypoint_web.sh"]