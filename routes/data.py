from flask import Blueprint, request, flash
from controllers.youtube_search import search_by_keyword, YouTubeData
from controllers.youtube_load import LoadVideos
from controllers.video_details import VideoDetails
from config import DB_DETAILS

search_youtube = Blueprint('search_keyword', __name__)

# request.args['search_by'])


@search_youtube.route('/keyword', methods=['GET'])
def data():
    if request.method == 'GET':
        param = ('request', request.args['search_by'])
        # request.args.get('search_by')
        if not param:
            error = 'Search Key word is Required'
        else:
            data = search_by_keyword(param)

    return data


@search_youtube.route('/key', methods=['GET'])
def search_keyword():
    if request.method == 'GET':
        param = ('request', request.args['search_by'])
        API_KEY = DB_DETAILS['API_KEY']['API_KEY']
        max_result = ('request', request.args['max_result'])

        if not param:
            error = 'Search Key word is Required'
        else:
            youTubeDataset = YouTubeData(API_KEY, param[1], max_result[1])
            filter = youTubeDataset.get_data_by_search_keyword()
            data = filter

    return {"data": data}


@search_youtube.route('/load-video', methods=['POST'])
def load_video():
    if request.method == 'POST':
        max_result = 40
        loadData = LoadVideos(max_result)
        filter = loadData.load_video()

        return{"data": filter}


@search_youtube.route('/video-details', methods=['GET'])
def load_details():
    if request.method == 'GET':
        get_videos = [3]
        fetchData = VideoDetails(get_videos)
        filter = fetchData.get_video_detail()
        return {"data": filter}
