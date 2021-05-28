FROM  python:3.7.4-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install nbconvert

ENV WORKDIR /app/
WORKDIR $WORKDIR
COPY . $WORKDIR

ENV TARGET ./input/report.ipynb
ENV OUTPUT_DIR ./output
ENV FIG_DIR_NAME ./fig

CMD ["sh", "-c", "python convert.py $TARGET $OUTPUT_DIR $FIG_DIR_NAME"]
