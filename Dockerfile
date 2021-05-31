FROM python:3.9-slim as conv
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    jq \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/

COPY ./mdconverter/Pipfile ./mdconverter/Pipfile.lock /app/

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

COPY . /app/

ARG WEBSITE_TARGET_DIRECTORY="website.config.json"
RUN mkdir target
RUN jq ".target.docs | .[]" $WEBSITE_TARGET_DIRECTORY \
    | xargs -I {} cp -r {} target/
RUN python mdconverter/convert.py target target fig
RUN find target -type f \
    | grep -i -v -E '.*\.(md|jpg|jpeg|png|gif)' \
    | xargs -I {} rm -f {}



FROM node:16-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV WORKDIR=/app/
WORKDIR ${WORKDIR}

ARG WEBSITE_DIRECTORY=website
COPY ${WEBSITE_DIRECTORY}/yarn.lock ${WEBSITE_DIRECTORY}/package.json ${WORKDIR}
RUN yarn install --frozen-lockfile

COPY $WEBSITE_DIRECTORY $WORKDIR
RUN rm -rf docs/
COPY --from=conv /app/target/ /app/docs/

COPY $WEBSITE_TARGET_DIRECTORY $WORKDIR

RUN yarn run build && \
    yarn cache clean

ENV PORT=80
ENV HOST=0.0.0.0
CMD ["sh", "-c", "yarn run serve --port $PORT --host $HOST"]
