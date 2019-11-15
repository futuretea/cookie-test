from flask import Flask
from flask import make_response, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response("root")
    resp.set_cookie('jsessionid', 'rooterr', path='/')
    resp.set_cookie('JSESSIONID', 'root', path='/')
    return resp


@app.route('/server1')
def server1():
    resp = make_response("sever1")
    resp.set_cookie('jsessionid', 'server1err', path='/server1')
    resp.set_cookie('JSESSIONID', 'server1', path='/server1')
    return resp


@app.route('/server2')
def server2():
    resp = make_response("server2")
    resp.set_cookie('jsessionid', 'server1err', path='/server2')
    resp.set_cookie('JSESSIONID', 'server2', path='/server2')
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)

