from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    demo = {"status":"success"}
    return jsonify(demo)

if __name__ == '__main__':
    app.run()