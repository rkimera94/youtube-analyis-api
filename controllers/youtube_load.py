from .youtube_search import YouTubeData
import requests
from config import DB_DETAILS
from flask import request

# from ..sql_database import Video, Session, engine
from sql_database import Video, Session, engine

local_session = Session(bind=engine)


class LoadVideos(object):
    def __init__(self, max_result):
        self.max_result = max_result

    def load_video(self):

        param = ('request', request.args['search_by'])
        API_KEY = DB_DETAILS['API_KEY']['API_KEY']
        max_result = ('request', request.args['max_result'])

        youTubeDataset = YouTubeData(API_KEY, param[1], max_result[1])
        filter = youTubeDataset.get_data_by_search_keyword()
        data = filter

        for v in data:

            video_id = v['id']
            if 'videoId' in video_id:
                insert_data = Video(
                    video_id=video_id['videoId'], kind=video_id['kind'])
                local_session.add(insert_data)
                local_session.commit()

        return {"message": "Data Loaded Successfully"}
