## about application

application is writen in python3 with help of django framework.
there are two implementation of date storage (redis and postgres).
to swith which implementation to use, navigate to *application.properties* file and change value of *service.db.relationional* correspondingly
## how to run

#### docker compose

this is the siplest way to run application
just make sure you have docker compose [installed](https://docs.docker.com/compose/install/#install-compose) on your computer, go to project's root directory in terminal and execute:

1. `docker-compose build`
2. `docker-compose up`

#### directly on machine

serving with *uwsgi*
make sure you have following packages installed
1. [python3](https://www.python.org/downloads/)
2. [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/Install.html)
3. [django](https://docs.djangoproject.com/en/3.0/topics/install/)
4. [redis](https://redis.io/topics/quickstart)
5. [postgres](https://www.postgresql.org/download/)
6. [pip](https://pip.pypa.io/en/stable/installing/)
7. [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
postgress and redis can be used without installing, you can use corresponding containers
create virtualenv in projects root directory, activate it and run `pip install -r requirements.txt`

after this steps setup postges and make sure that it has *postgres* user with *postgres* password , and *postgres* database

execute ```CREATE TABLE IF NOT EXISTS promotion (
    id SERIAL,
    external_id VARCHAR (36) ,
    price NUMERIC (5,2) NOT NULL,
    expiration_date  VARCHAR(100) NOT NULL 
);``` command to create table
start redis-server
navigate to `application.properties` file and change *redis port* and *host*: if you started *redis-server* on same machine, set value of *host* to *localhost*

to start web application execute ` uwsgi --ini configs/NginX/uwsgi.ini  --venv=/home/azatmanukyan/PycharmProjects/storage_problem/venv/` command in  terminal
to start worker application which is responsible vor data ingestion into postgress, execute `celery -A storage_problem worker --loglevel=info  --concurrency=1` command.

at this point you should be able to run application( if i'm not missing anyt)hing