FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD start.sh /code/
ADD . /code/
EXPOSE 80
CMD ["/code/start.sh"]