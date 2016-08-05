import os
from flask import Flask, request, jsonify
from jwt import encode, decode


app = Flask(__name__)

@app.route("/")
def hello():
    return "This is data from the back-end server!"

@app.errorhandler(400)
def known_error(error=None):
    app.logger.error("Bad request: '%s'", request.data.decode('UTF8'))
    message = {
        'status': 400,
        'message': "{}: {}".format(error, request.url),
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.errorhandler(500)
def unknown_error(error=None):
    app.logger.error("Error: '%s'", request.data.decode('UTF8'))
    message = {
        'status': 500,
        'message': "Internal server error: " + repr(error),
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp


@app.route('/token', methods=['GET'])
def profile():
    version = request.headers.get("Roadtrip-Version")
    user_id = request.headers.get("Roadtrip-UserId")
    accessToken = request.headers.get("Roadtrip-FacebookToken")
    # profile = request.get_json()
    print("version: " + repr(version))
    print("user_id: " + repr(user_id))
    print("accessToken: " + repr(accessToken))

    if user_id:
        token = encode({"user_id": user_id})
        return jsonify({"token": token})
    else:
        return known_error("Request payload was empty")


@app.route('/preferences', methods=['GET'])
def get_preferences():
    data = validate_token(request.headers.get("Roadtrip-Token"))

    if data:
        return jsonify(data)
    else:
        return known_error("Please provide a Roadtrip-Token header")


@app.route('/preferences', methods=['POST'])
def set_preferences():
    data = validate_token(request.headers.get("Roadtrip-Token"))

    if data:
        return jsonify(data)
    else:
        return known_error("Please provide a Roadtrip-Token header")


def validate_token(token):

    if token:
        data = decode(token)
        return data
    else:
        return ""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
