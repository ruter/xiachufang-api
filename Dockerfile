ARG INSTALL_PYTHON_VERSION=3.6
FROM python:${INSTALL_PYTHON_VERSION}-slim-buster AS base

RUN apt-get update
RUN apt-get install -y g++ libxml2-dev libxslt-dev python3-dev lib32z1-dev

WORKDIR /app
COPY . .

RUN useradd -m sid
RUN chown -R sid:sid /app
USER sid
ENV PATH="/home/sid/.local/bin:${PATH}"

RUN pip install --user -r requirements.txt

EXPOSE 5000
CMD ["python", "wsgi.py"]