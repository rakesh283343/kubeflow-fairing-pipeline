FROM google/cloud-sdk:latest

RUN cat /etc/os-release

WORKDIR /usr/src/app

COPY . .

COPY requirements.txt /
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "./code.py"]