# Web tupoj

### Installation
```
pip3 install -r requirements.txt

PYTHONUNBUFFERED=1
WEB2PY_VERSION=R-2.18.5
WEB2PY_ADMIN_SECURITY_BYPASS=true
WEB2PY_PASSWORD=pwd

python3 web2py.py -i 0.0.0.0 -p 8080 -a pwd
```

### Docker
```
docker build -t maslick/webtupoj .
docker run -d -p 8000:5000 -e BACKEND_URL=maslick.ru maslick/webtupoj
open http://`docker-machine ip`:8000
```
