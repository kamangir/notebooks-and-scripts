FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    psmisc \
    python3-pip \
    python3-venv \
    curl \
    git \
    rsync

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
RUN pip install pymysql
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

# to use the build version of <repo-name>,
#
# RUN mkdir -p /root/git/<repo-name>
# ADD ./<repo-name> /root/git/<repo-name>
# WORKDIR /root/git/<repo-name>
# RUN pip install -e .
#
# to use the latest built version of <module-name>,
#
# RUN pip install <module-name>

# blue-geo in dev mode
# TODO: remove this section and enable the pip install below.
RUN mkdir -p /root/git/blue-geo
ADD ./blue-geo /root/git/blue-geo
WORKDIR /root/git/blue-geo
RUN rm -v ./.env
RUN pip install -e .

# install blue packages
# https://chatgpt.com/share/f58db1ce-b2ee-4460-b0c8-24077113736c
RUN pip cache purge
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager blueness
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager blue-options
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager abadpour
# RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager blue_geo
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager blue_plugin
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager gizai
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager hubblescope
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager notebooks_and_scripts
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager openai_commands
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager vancouver-watching

# copy and install abcli 🪄
RUN pip uninstall -y abcli
RUN mkdir -p /root/git/awesome-bash-cli
ADD ./awesome-bash-cli /root/git/awesome-bash-cli
WORKDIR /root/git/awesome-bash-cli
RUN rm -v .env
RUN pip install -e .
