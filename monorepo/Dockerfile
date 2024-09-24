##########################################################
# Monorepo Docker Monolith
#
# This Dockerfile is used to build a monolith image
# that contains all of the code files in the monorepo.
# Dependencies are purposely not installed in this image,
# as it is intended to be used as the base image for all
# other images in the monorepo.
#
##########################################################

ARG PYTHON_VERSION=3.12
FROM ghcr.io/astral-sh/uv:python${PYTHON_VERSION}-bookworm-slim AS builder

# Set Working Directory
WORKDIR /root/work/

# Set Path to include Virtualenv
ENV PATH="/root/work/.venv/bin:${PATH}"
# UV Configuration
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

FROM builder AS base

# Instantiate Virtual Environment
RUN --mount=type=cache,target=/root/.cache/uv \
    uv venv --seed

# Copy Entire Monorepo Into Base Image
COPY . /root/work/

CMD ["/bin/bash"]
