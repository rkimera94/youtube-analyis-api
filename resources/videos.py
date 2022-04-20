from flask import request
from flask_restful import Resource
from controllers.youtube_load import LoadVideos


class VideoResource(Resource):
    def get(self):
        print('here')

    def post(self):
        max_result = 50
        get_videos = LoadVideos(max_result)
        data = get_videos.load_video()

        return {'status': 'success', 'data': data}, 200
