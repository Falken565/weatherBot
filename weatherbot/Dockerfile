FROM python:3.8

LABEL maintainer='falken'

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip &&\
    pip3 install gunicorn==20.0.4 &&\
    pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "weatherbot.wsgi", "-w", "4", "-t", "600", "-b", "0.0.0.0:8000"]