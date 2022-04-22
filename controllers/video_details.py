import requests
import pandas as pd
import json
from config import DB_DETAILS
from sql_database import Session, Video, engine
from schema.video import VideoDetailsSchema, video_details_schema, videos_details_schema

from models.video_details import VideoDetail, db, VideoTags, VideoDuration
from .video_class import VideoClass


BASE_url = DB_DETAILS['BASE_url']['BASE_url']
local_session = Session(bind=engine)
API_KEY = DB_DETAILS['API_KEY']['API_KEY']


class VideoDetails(object):
    def __init__(self, get_videos):
        self.get_videos = get_videos

    def get_video_detail(self):
        all_video_details = []

        filtered = local_session.query(Video).limit(2).all()

        data = videos_details_schema.dump(filtered)
        for v in data:
            videoId = v['video_id']
            url = f'{BASE_url}/videos?part=snippet&part=contentDetails&part=statistics&id={videoId}&key={API_KEY}'
            url_request = requests.get(url)
            json_data = json.loads(url_request.text)

            try:
                statistics = json_data['items'][0]['statistics']

                if 'contentDetails' in json_data['items'][0]:
                    duration = json_data['items'][0]['contentDetails']['duration']
                else:
                    duration = 0

                if 'tags' in json_data['items'][0]['snippet']:
                    tags = json_data['items'][0]['snippet']['tags']
                else:
                    tags = []

                id = json_data['items'][0]['id']

                kind = json_data['items'][0]['kind']

                video_dict = dict(

                    {"id": id, "kind": kind, "statistics": statistics, "tags": tags, "duration": duration})

                video_class = VideoClass(video_dict)
                video_tag = video_class.video_tag_load()
                video_tag = video_class.video_duration_load()

                video_stat = video_dict['statistics']

                insert_stat = VideoDetail(
                    video_id=video_dict['id'], view_count=video_stat['viewCount'], like_count=video_stat['likeCount'],
                    favorite_count=video_stat['favoriteCount'], comment_count=video_stat['commentCount'])

                db.session.add(insert_stat)

                db.session.commit()

                # result = videos_details_schema.dump(insert_stat).data
                # local_session.add(insert_data)
                # local_session.commit()

                all_video_details.append(video_dict)
            except Exception as error:
                #all_video_details = None
                return error

        return {'message': "Video Details Successfully Fetched", 'data': data}
