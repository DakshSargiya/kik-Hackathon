from flask import Flask
from flask import request
from mainProcess import getOptions
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

__name__ = "main"
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    if request.method == 'POST':
        data = request.json
        return getOptions(data.get("data"))
        # return do_the_login()
    else:
        return "<p>Hello, World!</p>"

if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000)
