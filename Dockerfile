FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY /custom custom
RUN pip install --upgrade pip
RUN pip install custom/

COPY /calypso calypso
RUN pip install -r calypso/requirements.txt

COPY .env .
EXPOSE 80

CMD ["uvicorn", "calypso.app.main:app", "--host", "0.0.0.0", "--port", "80"]