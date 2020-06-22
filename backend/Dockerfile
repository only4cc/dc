FROM python:3.7-slim
LABEL Julio Trumper S.

RUN mkdir -p backend-dir-en-docker

WORKDIR /

COPY requirements.txt /
ADD . /
RUN pip install -r /requirements.txt

EXPOSE 3000
CMD [ "python","app.py" ]

