import os

from fastapi import FastAPI

BRANCH = "case/build-error"

app = FastAPI()


@app.get("/")
def root():
    return {"branch": BRANCH, "lang": "python", "framework": "fastapi"}


@app.get("/healthz")
def healthz():
    return {"ok": True}
