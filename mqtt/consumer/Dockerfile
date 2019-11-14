FROM python:3.7

WORKDIR /app
ENV PYTHONPATH /app

COPY requirements.txt ./
COPY setup.py ./
COPY src/ /app/src
COPY test/ /app/test

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python setup.py test

CMD ["python", "src/main.py" ]