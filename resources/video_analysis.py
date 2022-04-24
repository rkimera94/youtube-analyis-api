from flask import request
from flask_restful import Resource
from flask import jsonify
import json

from controllers.data_analysis import VideoAnalysis


class VideoAnalysisResource(Resource):
    def get(self):
        video_analysis = VideoAnalysis()
        video_analysis_data = video_analysis.get_video_by_tags()

        # x = jsonify({'result': [dict(row) for row in video_analysis_data]})
        # x = jsonify(video_analysis_data)
        data = dict(video_analysis_data)

        print(dict(video_analysis_data))

        return {'status': 'success', 'data': data}, 200
