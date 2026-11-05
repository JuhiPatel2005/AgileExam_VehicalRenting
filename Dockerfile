FROM python:3.11

WORKDIR /exam

COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]