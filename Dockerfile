FROM python:3.11.5


WORKDIR /opt/epass

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . /opt/epass

EXPOSE 8000