FROM python:3.8

WORKDIR /srv

RUN mkdir -p /srv/service-discovery
VOLUME ["/srv/service-discovery"]

COPY requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt
COPY sd.py /srv/sd.py
RUN chmod +x /srv/sd.py

CMD ["python", "/srv/sd.py"]
