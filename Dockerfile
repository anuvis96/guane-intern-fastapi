FROM python:3.8-bullseye
WORKDIR /usr/src/app
COPY ./app .

COPY requirements.txt .
#ADD main.py /
RUN pip install -r ./requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]