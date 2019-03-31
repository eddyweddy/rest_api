FROM python:3.7-alpine
#FROM ubuntu:18.04
COPY . /app
COPY ./API /app
WORKDIR /app
# Install Python.
RUN set -ex \
  && apk add git \
  && pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["main.py"]
