FROM python:slim
MAINTAINER mikejoh
COPY preseeder/ /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["app.py"]
