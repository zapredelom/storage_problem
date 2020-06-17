from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from django.conf import settings

class MySQLAlchemySessionMiddleware(object):
    def process_request(self, request):
        request.db_session = settings.Session()

    def process_response(self, request, response):
        try:
            session = request.db_session
        except AttributeError:
            return response
        try:
            session.commit()
            return response
        except:
            session.rollback()
            raise

    def process_exception(self, request, exception):
        try:
            session = request.db_session
        except AttributeError:
            return
        session.rollback()