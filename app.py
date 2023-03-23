from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.snls57l.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/listing", methods=["GET"])
def list_task():
    tasks = list(db.tasks.find({}, {'_id': False}))
    return jsonify({'result': tasks})


@app.route("/add", methods=["POST"])
def add_task():
    name = request.form['name_give']
    content = request.form['content_give']

    doc = {'name': name, 'content': content}
    db.tasks.insert_one(doc)
    return jsonify({'result': '입력 완료!'})


@app.route("/delete", methods=["POST"])
def delete_task():
    name = request.form['name_give']

    db.tasks.delete_one({'name': name})
    return jsonify({'result': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
