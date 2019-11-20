FROM python:3.7

COPY . /app
WORKDIR /app
EXPOSE 5000

RUN pip3 install gunicorn && \
    pip3 install -r requirements.txt && \
    rm -fr applications/admin && \
    cp handlers/wsgihandler.py .

RUN useradd -m -r  web2py
USER web2py

CMD gunicorn wsgihandler:application -c gunicorn.config.py
