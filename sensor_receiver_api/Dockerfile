FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Creating workspace
ENV WORKSPACE=/usr/src/app
RUN mkdir -p $WORKSPACE
WORKDIR $WORKSPACE

# Project dependency
COPY ./sensor_receiver_api/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY ./sensor_receiver_api/ $WORKSPACE
