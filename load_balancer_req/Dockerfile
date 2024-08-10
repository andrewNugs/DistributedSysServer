FROM python:3.9-slim

WORKDIR /app

COPY load_balancer.py /app/

COPY consistent_hashing.py /app/

RUN pip install Flask docker

EXPOSE 5000

CMD ["python", "load_balancer.py"]
