from celery import shared_task
import billiard as mp
from django.conf import settings


from storage_problem.services.ServiceModels.Promotion import Promotion
from storage_problem.services import PromotionRelationService, PromotionService
from storage_problem.models.crud import sa_engine

service = PromotionRelationService.PromotionRelationService() if settings.USE_RELATIONAL_DB else PromotionService.PromotionService()

@shared_task
def load_data():
    pool = mp.Pool(8)
    jobs = []
    f = open('sample.csv','r',buffering=(2<<16))
    i = 0
    current_objects = []
    lines = f.readlines(100000)
    while lines:
        jobs.append(pool.apply_async(post_objects,[lines]))
        lines = f.readlines(100000)
    for job in jobs:
        job.get()

    #clean up
    pool.close()

@shared_task
def load_direct_from_csv():
    with open('sample.csv', 'rb') as f:    
        connection = sa_engine.raw_connection()
        cursor = connection.cursor()
        print('truncating table')
        cursor.execute('truncate table promotion')
        cmd = 'COPY promotion(external_id, price, expiration_date) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        print('importing data')
        cursor.copy_expert(cmd, f)
        print('creating index')
        cursor.execute('CREATE INDEX if not exists promotion_external_id_idx ON promotion (external_id);')
        print('commiting changes')
        connection.commit()
        print('closing connection')
        connection.close()
        print('connection closed')


def post_objects(lines):
    i = 0
    current_objects = []
    for line in lines:
        line = line.strip('\n')
        elems=line.split(',') 
        promotion = Promotion(id=None, external_id=elems[0] , price=elems[1],expiration_date=elems[2][0:-12])
        current_objects.append(promotion)
        i+=1
        if i == 100000:
            service.create_multiple(current_objects)
            current_objects = [] 
            i =0
    if len(current_objects) >0:
        service.create_multiple(current_objects)


def post_object(line):
    i = 0
    current_objects = []
    line = line.strip('\n')
    elems=line.split(',')
    promotion = Promotion(id=None, external_id=elems[0], price=elems[1],expiration_date=elems[2][0:-12])
    service.create(promotion)
