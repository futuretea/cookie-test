from flask import Flask
from flask import make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response("helloworld")
    resp.set_cookie('JSESSIONID', 'abcdef')
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)

