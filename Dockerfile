FROM python:latest

ARG NAME
WORKDIR /
COPY . /
CMD python3 main.py
