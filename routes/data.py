
from urllib import request
from flask import Blueprint
from controllers.youtube_search import search_by_keyword


search_youtube = Blueprint('search_keyword', __name__)


search_youtube.route('/keyword', methods=['GET'])(search_by_keyword)
