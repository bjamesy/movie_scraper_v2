FROM python:3.11

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]