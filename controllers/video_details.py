import requests
import pandas as pd
import json
from config import DB_DETAILS
from sql_database import Session, Video, engine
from schema.video import VideoDetailsSchema, video_details_schema, videos_details_schema

BASE_url = DB_DETAILS['BASE_url']['BASE_url']
local_session = Session(bind=engine)
API_KEY = DB_DETAILS['API_KEY']['API_KEY']


class VideoDetails(object):
    def __init__(self, get_videos):
        self.get_videos = get_videos

    def get_video_detail(self):
        get_video_details = []
        all_video_details = []

        filtered = local_session.query(Video).limit(3).all()
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

                all_video_details.append(video_dict)
            except:
                all_video_details = None

        # return {'data': "Video Details Successfully Fetched"}
        print(all_video_details)
        return data
