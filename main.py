import os

from fastapi import FastAPI

BRANCH = "case/containerfile"

app = FastAPI()


@app.get("/")
def root():
    return {"branch": BRANCH, "lang": "python", "framework": "fastapi", "dockerfile": os.environ.get("DOCKERFILE_SOURCE", "generated")}


@app.get("/healthz")
def healthz():
    return {"ok": True}
