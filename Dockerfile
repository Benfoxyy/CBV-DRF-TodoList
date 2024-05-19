# version of python
FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
# work directory
WORKDIR /app
# copy the requirements file to the working directory
COPY /core/requirements.txt /app/
# install all libraries in requirements.txt file
RUN pip3 install -r requirements.txt
# copy main app in directory
COPY ./core /app/