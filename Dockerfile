FROM ubuntu:latest

ENV container docker

WORKDIR /crypto

# Install and use latest versions of vim and conda
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y emacs

RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -n base -c defaults conda

# Install python packages via conda
COPY ./environment.yaml ./environment.yaml
RUN conda env create -f environment.yaml

# Ensure conda commands available when in container
RUN echo ". /miniconda/etc/profile.d/conda.sh" >> ~/.bashrc