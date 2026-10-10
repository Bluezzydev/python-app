import os

from fastapi import FastAPI

BRANCH = "py/version-311"

app = FastAPI()


@app.get("/")
def root():
    return {"branch": BRANCH, "lang": "python", "framework": "fastapi", "python": __import__("sys").version}


@app.get("/healthz")
def healthz():
    return {"ok": True}
