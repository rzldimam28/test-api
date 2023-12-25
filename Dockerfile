# Here is the build image
FROM python:3.11-slim as builder
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --user -r requirements.txt
# RUN pip install -r requirements.txt
COPY . /app

# Here is the production image
FROM python:3.11-slim as app
COPY --from=builder /root/.local /root/.local
RUN ls
# COPY --from=builder /app /app
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH