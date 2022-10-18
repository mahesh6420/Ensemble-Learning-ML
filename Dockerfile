FROM python:3.10-alpine
# FROM python:3.8-alpine
# FROM python:3.
# FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt
# RUN apt-get -y install libc-dev
# RUN apt-get -y install build-essential
RUN pip install -U pip
RUN pip install numpy
# RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 3000

# CMD ["flask", "run", "-p 3000"]
ENTRYPOINT [ "python" ]
CMD ["app.py"]