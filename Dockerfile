FROM python:3.7-slim
RUN mkdir www
COPY www www
RUN chmod a+rwx -R www
RUN pip install flask
RUN pip install flask-mysql
CMD cd /www && . venv/bin/activate && python app.py