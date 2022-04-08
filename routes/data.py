
from crypt import methods
from curses import flash, noecho
from distutils.log import error
from flask import Blueprint, request, flash
from controllers.youtube_search import search_by_keyword


search_youtube = Blueprint('search_keyword', __name__)

# request.args['search_by'])


@search_youtube.before_request
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
