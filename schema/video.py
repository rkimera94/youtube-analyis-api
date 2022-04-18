from flask_marshmallow import Marshmallow


ma = Marshmallow()


class VideoDetailsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'video_id', 'kind')


video_details_schema = VideoDetailsSchema()
videos_details_schema = VideoDetailsSchema(many=True)
