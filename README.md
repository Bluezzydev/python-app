# python-app: Koptan test fixtures

Every branch is an independent (orphan) app for one Koptan test scenario. Point a Service at it with `spec.source.revision: <branch>`; the IDs refer to `koptan-test-plan.md`.

Each app listens on `$PORT` (default 8080) and `GET /` names its branch, so `curl` shows what is deployed.

```yaml
apiVersion: koptan.felukka.org/v1
kind: Service
metadata:
  name: py-flask
  namespace: demo
spec:
  source:
    repo: https://github.com/Bluezzydev/python-app.git
    revision: py/flask
  port: 8080
```

| Branch | What it tests |
|---|---|
| `main` | Python FastAPI with `requirements.txt`. The default, happy-path app (SVC-03, SVC-11 tag `v1.0.0`). |
| `py/flask` | Flask app in `app.py`. Expect python/flask, started with gunicorn. |
| `py/django` | Django project `mysite`. Expect python/django, gunicorn `mysite.wsgi:application`. |
| `py/poetry` | FastAPI managed by Poetry (`[tool.poetry]` + `poetry.lock`). Expect package manager poetry. |
| `py/uv` | FastAPI managed by uv (`pyproject.toml` + `uv.lock`). Expect package manager uv. |
| `py/pipenv` | FastAPI managed by Pipenv (`Pipfile` + `Pipfile.lock`). Expect package manager pipenv. |
| `py/pyproject` | Standard-library app packaged with a bare `pyproject.toml` (no lock). Expect `pip install .` and `python main.py`. |
| `py/plain` | Standard-library HTTP server, empty `requirements.txt`, no framework. Expect `python main.py`. |
| `py/version-311` | FastAPI with `.python-version` = 3.11. Expect base image `python:3.11-slim`. |
| `lang/go` | Go, `main` package at the root, standard library only. Expect go, entrypoint `.`. |
| `lang/go-cmd` | Go with `cmd/server` and `cmd/worker`. Expect entrypoint `./cmd/server` (server is preferred). |
| `lang/node` | Node.js with a `start` script and `package-lock.json`. Expect node, `npm ci`, `npm run start`. |
| `lang/node-main` | Node.js without scripts or lockfile, entry `server.js`. Expect `npm install`, `node server.js`. |
| `lang/rust` | Rust, standard library only. Expect rust, binary `koptan-rust`. |
| `lang/java-maven` | Java 21 with Maven, JDK `HttpServer`, runnable jar. Expect java/maven. |
| `lang/java-gradle` | Java 21 with Gradle (no wrapper), runnable jar. Expect java/gradle, `gradle:8-jdk21`. |
| `lang/dotnet` | .NET 8 minimal API (Web SDK). Expect dotnet 8.0, assembly `KoptanDotnet`. |
| `lang/ruby` | Ruby Rack app served by Puma (`config.ru`). Expect ruby/rack, `puma -b tcp://0.0.0.0:$PORT`. |
| `lang/php` | Plain PHP `index.php`, no Composer. Expect php on `php:8.3-apache`. |
| `lang/static` | Static site, `index.html` at the root. Expect static (nginx-unprivileged). |
| `lang/static-public` | Static site in `public/`. Expect static with root `public`. |
| `case/own-dockerfile` | FastAPI with its own `Dockerfile` (SVC-06). Expect `dockerfileSource=repo`; the image has label `org.felukka.koptan-test.dockerfile=repo`. |
| `case/containerfile` | Same app with a `Containerfile` instead of a Dockerfile (SVC-07). |
| `case/docker-dir` | Same app with `docker/Dockerfile` (SVC-07). |
| `case/dockerfile-path` | Broken root `Dockerfile` plus a good `services/api/Dockerfile.prod` (SVC-08). Set `spec.build.dockerfilePath: services/api/Dockerfile.prod` (context: repo root). Without it: `no FROM instruction`. |
| `case/monorepo` | Monorepo: `services/api` (Python) and `services/web` (Node), nothing at the root (SVC-09). Use `spec.build.contextDir: services/api` or `services/web`; without it: no supported stack. |
| `case/ambiguous` | Both `requirements.txt` and `package.json` (SVC-10). Default detection: python (`main.py`). With `spec.build.language: node`: node (`server.js`). |
| `case/no-stack` | Only a README: no Dockerfile and no supported stack (SVC-30). Expect `no Dockerfile and no supported stack found`. |
| `case/no-from` | Dockerfile without a FROM line (SVC-38). Expect `no FROM instruction in the Dockerfile`. |
| `case/empty-dockerfile` | Empty Dockerfile (SVC-38). Expect `empty Dockerfile`. |
| `case/huge-dockerfile` | Valid Dockerfile padded past 256 KiB (SVC-38). Expect `the Dockerfile is larger than 262144 bytes`. |
| `case/symlink-escape` | `Dockerfile` is a symlink to `/etc/passwd` (SVC-40). Expect it refused; nothing outside the clone is read. |
| `case/build-error` | `requirements.txt` names a package that does not exist (CI-04). Expect CI `Failed` in build-push, pip error in `status.message`. |
| `case/crash` | App exits with code 1 at start (CD-02). Expect CrashLoopBackOff and CD not Running. |
| `case/wrong-port` | Ignores `$PORT` and listens on 9999 (CD-03). Expect pods Running but never Ready; CD stays Deploying. Works if `spec.port: 9999`. |
| `case/slow-start` | Sleeps 60 s before listening (CD-01). Expect CD `Deploying` for about a minute, then `Running`. |
| `case/env` | Returns `GREETING` and `APP_MODE` env vars (SVC-16). Set them in `spec.env` and `curl /`. |
| `case/vuln` | Deliberately vulnerable (PLG-05/06/11/12). Django 3.2.0 (critical CVEs, never imported) for trivy; command injection, unsafe YAML and SQL injection for CodeQL/SonarQube. NEVER expose this app. |
| `case/evil-filenames` | Normal app plus files whose names are shell syntax (PLG-13). Expect no command runs from a filename; check that no `pwned` file appears in plugin/build containers. |

`main` is tagged `v1.0.0` (SVC-11, revision = tag). Not covered by a branch: SVC-34 (an empty repository) and SVC-20 (push a new commit to `main` during the test).
