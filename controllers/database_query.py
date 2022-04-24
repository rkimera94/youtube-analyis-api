from unittest import result
from sqlalchemy import text
# from ..sql_database import engine

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


Base = declarative_base()

'''
class to store  video ids
'''
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# database connection params
db_user = os.getenv("DB_USERNAME")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_DATABASE_NAME")

'''
config database connection
    - connection string 
    - create sqlalchemy engine 
'''

connection_string = f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}'


engine = create_engine(connection_string, echo=True)


class DataAnalysisQueries(object):
    @staticmethod
    def video_by_tags():
        try:
            sql = text(
                'select tag as tag,count(*) as number_of_videos from video_tags group by tag')
            result = engine.execute(sql).fetchall()

            return result

        except Exception as error:
            return error
