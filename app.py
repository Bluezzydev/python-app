# Deliberately vulnerable test app for scanner plugins. Do not deploy publicly.
import sqlite3
import subprocess

import yaml
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def root():
    return jsonify(branch="case/vuln", lang="python", framework="flask")


@app.get("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    out = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True, text=True)
    return out.stdout


@app.post("/config")
def config():
    data = yaml.load(request.data, Loader=yaml.Loader)
    return jsonify(loaded=str(data))


@app.get("/user")
def user():
    name = request.args.get("name", "")
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (name TEXT)")
    rows = db.execute("SELECT * FROM users WHERE name = '%s'" % name).fetchall()
    return jsonify(rows=rows)
