FROM node:16-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    jq \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV WORKDIR /app/

WORKDIR ${WORKDIR}

COPY ./website/yarn.lock ./website/package.json ${WORKDIR}

RUN yarn install --frozen-lockfile

COPY ./ $WORKDIR

RUN mv -f ./website/* ./ && \
    rm -rf ./website

RUN echo ${ARG} && \
    cat ${ARG}

RUN yarn run build && \
    yarn cache clean

ARG WEBSITE_TARGET_DIRECTORY=website.config.json
RUN jq ".target.docs | .[]" website.config.json \
    | xargs -I {} sh -c "mv -f {}/* ./docs && rm -rf {}"

ENV PORT=80
ENV HOST=0.0.0.0
CMD ["sh", "-c", "yarn run serve --port $PORT --host $HOST"]
