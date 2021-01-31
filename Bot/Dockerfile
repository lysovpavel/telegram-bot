FROM python:3.7

RUN mkdir -p /source/
WORKDIR /source/
COPY . /source/
RUN pip install --no-cache-dir -r requirements.txt

CMD python bot.py

