FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install .

EXPOSE 8080

CMD ["python3", "src/autosuggest/app.py"]