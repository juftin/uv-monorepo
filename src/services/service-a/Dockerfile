ARG PYTHON_VERSION=3.12
ARG DOCKER_REPO_NAME=uv-monorepo
ARG MONOREPO_DOCKER_IMAGE_NAME=uv-monorepo
ARG MONOREPO_DOCKER_IMAGE_TAG=latest

FROM ${DOCKER_REPO_NAME}/${MONOREPO_DOCKER_IMAGE_NAME}:${MONOREPO_DOCKER_IMAGE_TAG} AS builder

ARG PACKAGE_NAME

# Sync the Dependencies First to Utilize Docker Layer Caching
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync \
    --no-install-project \
    --locked \
    --no-editable \
    --no-dev \
    --package ${PACKAGE_NAME}
# Sync the Project Files
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync \
    --locked \
    --no-editable \
    --no-dev \
    --package ${PACKAGE_NAME}

FROM python:${PYTHON_VERSION}-slim-bookworm AS final

COPY --from=builder --chown=root:root /root/work/.venv/ /root/work/.venv/

WORKDIR /root/work/

ENV PATH="/root/work/.venv/bin:${PATH}"

CMD ["uvicorn", "service_a.app:app", "--host", "0.0.0.0", "--port", "8000"]
