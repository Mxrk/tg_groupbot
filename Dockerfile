FROM python:3.7 as builder

WORKDIR /usr/src/bot
COPY . /usr/src/bot
RUN pip3 install --no-cache-dir -r requirements.txt 


FROM python:3.7-alpine 
WORKDIR /usr/src/bot
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/src/bot /usr/src/bot

CMD [ "python3", "./main.py" ]