FROM python:3.12-slim
LABEL org.felukka.koptan-test.dockerfile="repo"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt uvicorn
COPY . .
ENV PORT=8080 DOCKERFILE_SOURCE=repo
USER 10001:10001
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
