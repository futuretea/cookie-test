from flask import Flask
from flask import make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    cookies = request.cookies
    v = cookies.get('JSESSIONID', "")
    resp = make_response(v)
    resp.set_cookie('JSESSIONID', 'abcdef')
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)

