#from sqlalchemy.orm import declarative_base
from curses import echo
from datetime import datetime
from email.encoders import encode_noop
from sqlalchemy import Column, String, DateTime, Integer, create_engine
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

# engine = create_engine(
#     f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}')


engine = create_engine(connection_string, echo=True)

# session maker
Session = sessionmaker()

''' Video class'''


class Video(Base):
    __tablename__ = 'yt_videos'
    id = Column(Integer(), primary_key=True)
    video_id = Column(String(), unique=True)
    kind = Column(String(255), nullable=True)
    title = Column(String(255), nullable=True)
    channel_title = Column(String(255), nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):

        return f"<video video_id ={self.video_id}"


new_video = Video(id=1, video_id='352yu493430', kind='DEMO')

print('new_video', new_video)
