FROM alpine:latest
LABEL description='WG BOT'

RUN apk update && apk upgrade && apk add --no-cache build-base && apk add --no-cache bash && apk add --no-cache python3 && apk add py3-pip && apk add --no-cache py3-greenlet
WORKDIR /opt/WGBOT

