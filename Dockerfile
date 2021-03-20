FROM ubuntu:20.04

WORKDIR ./profiles-rest-api

COPY requirements.txt ./
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip3 install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

ENV PORT=8000

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]