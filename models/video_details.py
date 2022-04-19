from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, pre_load, validate


db = SQLAlchemy()
ma = Marshmallow()


class Video(db.Model):
    __tablename__ = 'yt_videos'
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(255), unique=True)
    kind = db.Column(db.String(255), nullable=True)
    created_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)


class VideoDetail(db.Model):
    __tablename__ = 'video_details'

    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(255), db.ForeignKey(
        'yt_videos.video_id'), unique=True,)
    view_count = db.Column(db.Integer)
    like_count = db.Column(db.Integer)
    favorite_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    created_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    video = db.relationship("Video", backref="video_details")

    def __init__(self, id, view_count, like_count, favorite_count, comment_count):
        self.id = id
        self.view_count = view_count
        self.like_count = like_count
        self.favorite_count = favorite_count
        self.comment_count = comment_count


class VideoDetailSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    view_count = fields.Integer(required=True)
    like_count = fields.Integer(required=True)
    favorite_count = fields.Integer(required=True)
    comment_count = fields.Integer(required=True)
    video_id = fields.String(required=True, validate=validate.Length(1))
    created_at = fields.DateTime()
