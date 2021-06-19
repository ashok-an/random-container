FROM python:3.8-slim-buster

WORKDIR /app
RUN pip3 install flask
COPY ./app.py /app
COPY ./templates/ /app/templates/

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
