FROM python:3.7

RUN mkdir -p /source/
WORKDIR /source/
COPY . /source/
RUN pip install --no-cache-dir -r requirements.txt

ENV TZ Europe/Moscow

EXPOSE 5000

CMD python main.py

