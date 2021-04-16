FROM python:3.8

RUN mkdir -p /source/
WORKDIR /source/
COPY venv/lib/python3.8/site-packages /source/
RUN pip install --no-cache-dir -r requirements.txt

CMD python bot.py

