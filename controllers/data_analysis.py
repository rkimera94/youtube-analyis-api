import requests
import pandas as pd
import json
from .database_query import DataAnalysisQueries


class VideoAnalysis(object):

    @staticmethod
    def get_video_by_tags():
        result = DataAnalysisQueries()
        filtered = result.video_by_tags()
        return filtered
