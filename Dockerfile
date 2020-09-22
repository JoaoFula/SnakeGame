FROM python:3.8.2

WORKDIR /code

ENV PORT 80

COPY requirements.txt /code/requirements.txt

RUN apt-get update
RUN apt-get install -y libsdl1.2-dev libsdl-image1.2-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libportmidi-dev
RUN pip3 install pygame

COPY . /code

CMD ["python","./main.py"]