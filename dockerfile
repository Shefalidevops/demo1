FROM python:3.13-alpine

# RUN apt update
# RUN apt install python3-pip -y
RUN pip install flask

WORKDIR /app

COPY . .

CMD ["python3" , "main.py", "0.0.0.0", "8000"]