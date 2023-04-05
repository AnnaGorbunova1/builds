FROM python:3.10-alpine
WORKDIR /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN mkdir /builds
WORKDIR /builds
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]