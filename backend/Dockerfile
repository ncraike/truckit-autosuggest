FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install .

EXPOSE 7000

CMD ["python3", "src/autosuggest/app.py"]