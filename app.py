from flask import Flask, jsonify

BRANCH = "py/flask"

app = Flask(__name__)


@app.get("/")
def root():
    return jsonify(branch=BRANCH, lang="python", framework="flask")


@app.get("/healthz")
def healthz():
    return jsonify(ok=True)
