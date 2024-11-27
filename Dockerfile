FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]