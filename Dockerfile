FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install gunicorn && \
    pip3 install -r requirements.txt

COPY . /app

RUN rm -fr applications/admin && \
    cp handlers/wsgihandler.py .

RUN useradd -m -r  web2py
USER web2py
EXPOSE 5000

CMD ["gunicorn", "wsgihandler:application", "-c", "gunicorn.config.py"]
