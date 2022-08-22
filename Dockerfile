FROM python:3.10-alpine

COPY requirements.txt requirements.txt
COPY ./app /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]