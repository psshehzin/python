from flask import Flask
app = Flask(__name__)
@app.route("/")
def test():
    return "Hi There"
@app.route("/v1")
def hello():
    return "kollam poli sanam"
if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8081)
