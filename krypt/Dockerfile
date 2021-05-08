FROM python:3.7 as buildbase

COPY custom/ custom/
RUN pip install --upgrade pip
RUN pip install custom/

COPY /krypt /krypt
WORKDIR /krypt
RUN pip install -r requirements.txt

CMD ["bash", "/scripts/start.sh"]