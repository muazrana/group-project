FROM python:2.7
RUN apt update
RUN apt install -y netcat
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["./init.sh"]
