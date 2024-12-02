FROM apache/airflow:2.7.0
RUN pip install pyspark pandas matplotlib scikit-learn
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
