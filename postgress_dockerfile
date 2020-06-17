FROM postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres
ADD sample.csv /sample.csv
ADD createTable.sql /docker-entrypoint-initdb.d/
