from flask import Flask
from routes.data import search_youtube

app = Flask(__name__)


app.register_blueprint(search_youtube, url_prefix='/search')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
