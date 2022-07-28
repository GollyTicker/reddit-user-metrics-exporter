FROM python:slim
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY *.py ./
CMD python main.py
