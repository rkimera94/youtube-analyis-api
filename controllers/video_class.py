import requests
import pandas as pd
import json

from models.video_details import VideoDetail, db, VideoTags, VideoDuration
from .duration_convertion import DurationConvertion


class VideoClass(object):
    def __init__(self, video):
        self.video = video

    def video_duration_load(self):
        video_dict = self.video

        video_duration = self.video['duration']

        duration_convertion = DurationConvertion(video_duration)
        duration_convert = duration_convertion.duration_convertion()

        insert_duration = VideoDuration(
            video_id=video_dict['id'], video_duration=duration_convert)

        db.session.add(insert_duration)

    def video_tag_load(self):
        video_dict = self.video
        tags = video_dict['tags']
        for i in range(len(tags)):
            row = tags[i]
            try:
                insert_tag = VideoTags(
                    video_id=video_dict['id'], tag=row)
                db.session.add(insert_tag)

            except Exception as error:
                return error
        # db.session.commit()
