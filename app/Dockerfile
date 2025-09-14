FROM python:3.13-alpine

# RUN apt update
# RUN apt install python3-pip -y
RUN pip install flask

WORKDIR /app

COPY . .
RUN mkdir -p /app/logs

CMD ["python3" , "main.py", "--host=0.0.0.0", "--port=8000"] 