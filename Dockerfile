from python:3.7-alpine

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev \
    cmake \
    gcc \
    libxml2 \
    automake g++\ 
    subversion\
    libxml2-dev \
    libxslt-dev \
    lapack-dev \
    gfortran \
    openblas

#RUN apk add py3-scipy

RUN pip install pillow 
RUN pip install numpy 
RUN pip install matplotlib imageio 
RUN apk add lapack openblas-dev lapack-dev 
RUN pip install scipy==1.3.1

RUN mkdir /usr/local/lib/python3.7/site-packages/btb_tools_templates

COPY btb_tools_templates/* /usr/local/lib/python3.7/site-packages/btb_tools_templates/

CMD tail -f /dev/null