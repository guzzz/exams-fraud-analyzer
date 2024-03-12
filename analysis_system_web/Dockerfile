FROM python:3.11.3

# Creating workspace
ENV WORKSPACE=/usr/src/app
RUN mkdir -p $WORKSPACE
WORKDIR $WORKSPACE

# Project dependency
RUN pip install --upgrade pip
COPY ./analysis_system_web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY ./analysis_system_web/ $WORKSPACE
