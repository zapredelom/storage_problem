from sqlalchemy.ext.declarative import declarative_base
import redis

Base = declarative_base()
# redis_session=redis.Redis(host='localhost', port=6379, db=0)