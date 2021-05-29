FROM python:3.9-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV WORKDIR /app/
WORKDIR $WORKDIR

COPY Pipfile Pipfile.lock ${WORKDIR}

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

COPY . $WORKDIR

ENV TARGET ./input/report.ipynb
ENV OUTPUT_DIR ./output
ENV FIG_DIR_NAME ./fig

CMD ["sh", "-c", "python convert.py $TARGET $OUTPUT_DIR $FIG_DIR_NAME"]
