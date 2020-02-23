from app import app, mongo
from flask import jsonify, request


@app.route('/healthcheck')
def healthcheck():
    return jsonify(message="Healthy!"), 200


@app.route('/tweet', methods=['POST'])
def add_tweet():
    _json = request.json
    _name = _json['name']
    _tweet = _json['message']

    mongo.db.tweets.insert({'name': _name, 'tweet': _tweet})
    return jsonify('Tweet added successfully!')


@app.route('/feed')
def feed():
    messages = mongo.db.tweets.find()
    output = []
    for message in messages:
        output.append({'name': message['name'], 'tweet': message['tweet']})
    return jsonify({'result': output})


@app.errorhandler(404)
def not_found(error=None):
    return jsonify(message='Not Found: ' + request.url), 404


if __name__ == "__main__":
    app.run()
