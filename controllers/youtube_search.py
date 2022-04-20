import requests
import pandas as pd
import json
from config import DB_DETAILS


def search_by_keyword(search_key):
    print(search_key)
    return search_key


class YouTubeData:
    def __init__(self, api_key, search_keyword, max_result):
        self.api_key = api_key
        self.max_result = max_result
        self.search_keyword = search_keyword
        self.search_youtube_data = None

    def get_data_by_search_keyword(self):

        url = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q={self.search_keyword}&type=video&key={self.api_key}&maxResults={self.max_result}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items']
            print('Number of videos', len(data))

        except:
            data = None
        self.search_youtube_data = data

        return data

    # function to dump data into the json file

    def dump_file(self):
        if self.search_youtube_data is None:
            return
        # api data
        search_keyword = self.search_keyword.replace(" ", "_").lower()

        file_name = search_keyword + '.json'
        videos_file_name = search_keyword+'_videos' + '.json'

        with open(file_name, 'w') as f:

            json.dump(self.search_youtube_data, f, indent=4)

        print('file dumped')

    def dump_video_file(self):
        if self.search_youtube_data is None:
            return
        # api data
        search_keyword = self.search_keyword.replace(" ", "_").lower()
        # array of video data
        videos = []
        videoData = self.search_youtube_data
        for index in range(len(videoData)):

            videos.append(videoData[index]['id'])

        videos_file_name = search_keyword+'_videos' + '.json'

        with open(videos_file_name, 'w') as f:
            videos = videos
            json.dump(videos, f, indent=4)
        print('Video  Data Stored')
