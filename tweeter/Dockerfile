FROM python:3.7

RUN apt-get update \
    && apt-get install -y \
       bash curl nano net-tools zip unzip \
       dnsutils iputils-ping

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - \
    && wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - \
    && echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list \
    && apt-get update \
    && apt-get install -y mongodb-org

RUN mkdir -p /data/db /etc/consul.d

ADD https://releases.hashicorp.com/consul/1.7.0/consul_1.7.0_linux_amd64.zip /tmp/consul.zip
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

ADD https://github.com/mattn/goreman/releases/download/v0.3.4/goreman_linux_amd64.zip /tmp/goreman.zip
RUN cd /bin && unzip /tmp/goreman.zip && chmod +x /bin/goreman && rm /tmp/goreman.zip

COPY ./consul /etc/consul.d
COPY Procfile /root/Procfile
COPY consul.sh /opt

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposing appropriate ports
EXPOSE 5000/tcp

ENTRYPOINT [ "goreman" ]
CMD [ "-f", "/root/Procfile", "start" ]
