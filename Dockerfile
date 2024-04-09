FROM ubuntu:latest

RUN apt-get update && apt-get install -y psmisc

RUN apt-get update && apt-get install -y python3-pip

RUN pip install numpy
RUN pip install panda
RUN pip install geojson
RUN pip install beautifulsoup4
RUN pip install geopandas
RUN pip install tqdm
RUN pip install pymysql==0.10.1
RUN pip install boto3
RUN pip install python-dotenv[cli]

# https://askubuntu.com/a/1013396/1590785
ARG DEBIAN_FRONTEND=noninteractive

# https://stackoverflow.com/a/66473309/17619982
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

RUN apt install -y awscli

RUN mkdir -p /root/git/awesome-bash-cli
ADD ./awesome-bash-cli /root/git/awesome-bash-cli
WORKDIR /root/git/awesome-bash-cli
RUN pip install -e .

RUN mkdir -p /root/git/notebooks-and-scripts
ADD ./notebooks-and-scripts /root/git/notebooks-and-scripts
WORKDIR /root/git/notebooks-and-scripts
RUN pip install -e .

RUN mkdir -p /root/git/Vancouver-Watching
ADD ./Vancouver-Watching /root/git/Vancouver-Watching
WORKDIR /root/git/Vancouver-Watching
RUN pip install -e .
