FROM python:3.8-slim

WORKDIR /streamlit

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./streamlit_app.py ./streamlit_app.py
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["streamlit", "run", "/streamlit/streamlit_app.py"]