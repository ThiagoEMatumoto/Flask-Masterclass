from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/posts'>Posts</a>"

@app.route("/posts")
def posts():
    data = dict(path=request.path,
            referrer=request.referrer,
            content_type=request.content_type,
            method=request.method)
    return data



if __name__ == "__main__":
    app.run()


