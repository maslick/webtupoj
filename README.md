# =Web tupoj=

[![image size](https://img.shields.io/badge/image%20size-340MB-blue.svg)](https://hub.docker.com/r/maslick/webtupoj)

## Features
* Stripped down version of the base w2p app
* Dev mode friendly (admin console)
* Served by [Gunicorn](https://gunicorn.org/)
* Naked URL i.e. ``http://localhost:8080``, no extra URL paths
* Dockerfile + k8s

## Installation
```
pip3 install -r requirements.txt

PYTHONUNBUFFERED=1
WEB2PY_VERSION=R-2.18.5
WEB2PY_ADMIN_SECURITY_BYPASS=true
WEB2PY_PASSWORD=pwd

python3 web2py.py -i 0.0.0.0 -p 8080 -a pwd
```

## Testing
* Unit testing
```
python3 -m unittest discover applications/webtupoj/tests/unit
```

* Integration testing
```
python3 web2py.py -i 0.0.0.0 -p 8080 -a pwd
python3 -m unittest discover applications/webtupoj/tests/integration
```

## Docker
```
docker build -t maslick/webtupoj .
docker run -d -p 8000:5000 -e BACKEND_URL=maslick.ru maslick/webtupoj
open http://`docker-machine ip`:8000
```

## k8s
```
kubectl apply -f k8s
k set env deploy citatos BACKEND_URL=www.goog.li
open http://webtupoj.maslick.io
```
