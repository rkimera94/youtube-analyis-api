from flask import Flask, request
from routes.data import search_youtube


app = Flask(__name__)


app.register_blueprint(search_youtube, url_prefix='/search')


@app.route("/")
def hello_world():

    params = request.query_string
    params_x = request.args['x']
    print(params_x)
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
