#from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

'''
class to store  video ids
'''


class Video(Base):
    __tablename__ = 'yt_videos'
    id = Column(Integer(), primary_key=True)
    video_id = Column(String(), unique=True)
    kind = Column(String(255), nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):

        return f"<video video_id ={self.video_id}"


new_video = Video(id=1, video_id='47634759', kind='DEMO')

print('new_video', new_video)
