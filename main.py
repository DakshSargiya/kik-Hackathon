import json
from flask import Flask
from flask import request
from mainProcess import getOptions
__name__ = "main"
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.json
        return getOptions(data.get("data"))
        # return do_the_login()
    else:
        return "<p>Hello, World!</p>"
