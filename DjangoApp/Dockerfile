# syntax=docker/dockerfile:1
FROM python:3

# set environment variables
ENV PYTHONUNBUFFERED=1

# create directories
WORKDIR /code
COPY requirements.txt /code/

# Install requirements
RUN pip install -r requirements.txt

# copy project
COPY . /code/

# These line for /entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
entrypoint "/entrypoint.sh"

# Expose Port 
EXPOSE  8000

# Entrypoint
CMD         []
ENTRYPOINT  ["/entrypoint.sh"]