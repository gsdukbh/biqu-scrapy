FROM  python:3.8-alpine
WORKDIR /app
COPY . /app
RUN pip3 install --default-timeout=600  scrapy pymongo pymysql scrapy-redis 

CMD [ "python", "./my/main.py ]
