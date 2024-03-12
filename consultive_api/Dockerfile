FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Creating workspace
ENV WORKSPACE=/usr/src/app
RUN mkdir -p $WORKSPACE
WORKDIR $WORKSPACE

# Project dependency
COPY ./consultive_api/requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project
COPY ./consultive_api/ $WORKSPACE
