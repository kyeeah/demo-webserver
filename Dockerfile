FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 

COPY app app

# gunicorn 으로 web 실행하기
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8000", "app.app:app"]
