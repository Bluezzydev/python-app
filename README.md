# python-app @ `case/dockerfile-path`

Broken root `Dockerfile` plus a good `services/api/Dockerfile.prod` (SVC-08). Set `spec.build.dockerfilePath: services/api/Dockerfile.prod` (context: repo root). Without it: `no FROM instruction`.

See the `main` branch README for every branch.
