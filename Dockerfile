FROM python:3.8-bullseye
WORKDIR /usr/src/app
COPY requirements.txt .
#ADD main.py /
RUN pip install -r ./requirements.txt
COPY . .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload" ]