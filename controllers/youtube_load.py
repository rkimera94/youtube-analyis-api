from youtube_search import YouTubeData
import request
from config import DB_DETAILS


class LoadVideos(object):
    def __init__(self, api_key, data):
        self.api_key = api_key
        self.data = data

    def load_video(self):

        param = ('request', request.args['search_by'])
        API_KEY = DB_DETAILS['API_KEY']['API_KEY']
        max_result = ('request', request.args['max_result'])

        youTubeDataset = YouTubeData(API_KEY, param[1], max_result[1])
        filter = youTubeDataset.get_data_by_search_keyword()
        data = filter

        print(data)
        # if self.data is None:
        #     print('data')
