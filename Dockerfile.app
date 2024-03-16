FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 5001

CMD ["python", "myApp.py"]
