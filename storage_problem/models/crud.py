from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from django.conf import settings

sa_engine = create_engine(settings.DB_CONNECTION_URL,pool_size=100, max_overflow=0)  
Session = sessionmaker(bind=sa_engine)