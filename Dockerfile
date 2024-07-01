FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    psmisc \
    python3-pip \
    python3-venv \
    curl

# Create a virtual environment to isolate our package installations
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages using pip in the virtual environment
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install geojson
RUN pip install beautifulsoup4
RUN pip install geopandas
RUN pip install tqdm
RUN pip install pymysql==0.10.1
RUN pip install boto3
RUN pip install python-dotenv[cli]
RUN pip install matplotlib
RUN pip install networkx
RUN pip install pydot

# https://askubuntu.com/a/1013396/1590785
ARG DEBIAN_FRONTEND=noninteractive

# Install OpenCV from the Ubuntu repositories
# https://stackoverflow.com/a/66473309/17619982
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

RUN pip install awscli
RUN pip install setuptools

RUN pip install --no-cache-dir blueness
RUN pip install --no-cache-dir abadpour
RUN pip install --no-cache-dir blue_geo
RUN pip install --no-cache-dir blue_plugin
RUN pip install --no-cache-dir openai_commands
RUN pip install --no-cache-dir gizai

# Copy and install local packages
RUN mkdir -p /root/git/awesome-bash-cli
ADD ./awesome-bash-cli /root/git/awesome-bash-cli
WORKDIR /root/git/awesome-bash-cli
RUN pip install -e .

RUN mkdir -p /root/git/notebooks-and-scripts
ADD ./notebooks-and-scripts /root/git/notebooks-and-scripts
WORKDIR /root/git/notebooks-and-scripts
RUN pip install -e .

RUN mkdir -p /root/git/vancouver-watching
ADD ./vancouver-watching /root/git/vancouver-watching
WORKDIR /root/git/vancouver-watching
RUN pip install -e .
