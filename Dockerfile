FROM python:2.7
RUN apt update
RUN apt install git -y
RUN apt install python3 -y
RUN apt install python3-pip -y
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["["/usr/bin/python3", "run.py"]
