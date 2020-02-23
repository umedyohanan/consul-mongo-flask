FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    bash curl nano net-tools zip unzip \
    jq dnsutils iputils-ping file

RUN apt-get install -y mongodb

RUN mkdir -p /data/db /etc/consul.d

ADD https://releases.hashicorp.com/consul/1.7.0/consul_1.7.0_linux_amd64.zip /tmp/consul.zip
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

ADD https://github.com/mattn/goreman/releases/download/v0.3.4/goreman_linux_amd64.zip /tmp/goreman.zip
RUN cd /bin && unzip /tmp/goreman.zip && chmod +x /bin/goreman && rm /tmp/goreman.zip

VOLUME data:/data/db

COPY ./consul /etc/consul.d

COPY mongo.sh /opt
COPY mongo-init.js /opt
COPY mongo-init-tweets.js /opt
COPY consul.sh /opt
COPY Procfile /root/Procfile

EXPOSE $MONGO_PORT

ENTRYPOINT [ "goreman" ]
CMD [ "-f", "/root/Procfile", "start" ]