FROM python:3.10.6-buster

COPY requirements.txt /requirements.txt
COPY cg_interface /cg_interface
COPY cg_api /cg_api
COPY openapi /openapi
COPY recommendation /recommendation

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn cg_api.fast_api:app --host 0.0.0.0
