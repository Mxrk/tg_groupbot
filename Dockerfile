FROM python:3.7-alpine as builder

WORKDIR /usr/src/bot
COPY . /usr/src/bot
RUN apk add -U --no-cache gcc build-base linux-headers python3-dev libffi-dev libressl-dev libxslt-dev
RUN pip3 install --no-cache-dir -r requirements.txt 


FROM python:3.7-alpine 
WORKDIR /usr/src/bot
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/src/bot /usr/src/bot

CMD [ "python3", "./main.py" ]