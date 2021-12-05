#Deriving the latest base image
FROM ubuntu:16.04
FROM python:3.8.3

RUN apt-get update -y && \
	apt-get install -y python-pip python-dev
	




# Any working direcrtory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY test.py ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./test.py"]