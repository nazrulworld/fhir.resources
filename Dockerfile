FROM python:3.7-slim

LABEL name="FHIR Resources" \
    description="All FHIR Resources are available as python class with built-in initial validation, exporter as json value." \
    maintainer="Md Nazrul Islam"

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Install Python Setuptools
RUN apt-get update -y && \
    apt-get install -y locales git-core gcc g++ netcat libxml2-dev \
    libxslt-dev libz-dev python3-dev libyaml-dev

RUN mkdir /fhir_resources
COPY . /fhir_resources
RUN pip install -U pipenv
RUN cd /fhir_resources && pipenv install --dev && pipenv run pytest fhir/resources/tests
RUN cd /fhir_resources && pipenv run pytest fhir/resources/STU3/tests
