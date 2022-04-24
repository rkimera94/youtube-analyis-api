from flask import request
from flask_restful import Resource
from models.video_details import db, VideoDetailSchema, VideoDetail
from controllers.video_details import VideoDetails


video_details_schema = VideoDetailSchema()
videos_details_schema = VideoDetailSchema(many=True)


class VideoDetailsResource(Resource):
    def get(self):
        videoDetails = VideoDetail.query.all()
        videoDetails = videos_details_schema.dump(videoDetails)
        return {'status': 'success', 'data': videoDetails}, 200

    def post(self):
        get_videos = [8]
        get_video_details = VideoDetails(get_videos)
        data = get_video_details.get_video_detail()

        return {'status': 'success', 'data': data}, 200
