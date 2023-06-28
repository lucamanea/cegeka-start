FROM python:3.9-alpine

COPY ./requirements.txt /main/requirements.txt

WORKDIR /main

RUN pip install -r requirements.txt

COPY . /main

CMD ["flask", "run", "-h", "0.0.0.0"]
