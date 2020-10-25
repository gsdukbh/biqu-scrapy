FROM  python:3.8-alpine
LABEL MAINTAINER https://github.com/gsdukbh/biqu-scrapy
WORKDIR /app
COPY . /app
RUN pip install   scrapy && pip install  pymongo && pip intall  pymysql && pip install  scrapy-redis 

CMD [ "python", "./my/main.py ]
