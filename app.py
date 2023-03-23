from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.snls57l.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# doc = {'name': 'test', 'content': 'test'}
# db.tasks.insert_one(doc)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/listing", methods=["GET"])
def members_get():
    tasks = list(db.tasks.find({}, {'_id': False}))
    return jsonify({'result': tasks})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
