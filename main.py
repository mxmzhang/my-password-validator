import flask


# TODO: change this to your academic email
AUTHOR = "meganzh@seas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")
    if len(pw) < 8: return flask.jsonify({"valid": False, "reason": "Too short"}), 400
    upper = 0
    digit = 0
    special = 0
    for c in pw:
        if c.isupper(): upper += 1
        if c.isdigit(): digit += 1
        if c in "!@#$%^&*": special += 1
    if upper < 2: return flask.jsonify({"valid": False, "reason": "Not enough uppercase letters"}), 400
    if digit < 2: return flask.jsonify({"valid": False, "reason": "Not enough digits"}), 400
    if special < 1: return flask.jsonify({"valid": False, "reason": "Special character missing"}), 400
    return flask.jsonify({"valid": True, "reason": "Password valid"}), 200
