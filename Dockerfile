# No FROM on purpose.
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
