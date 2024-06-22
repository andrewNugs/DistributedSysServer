# Variables
DOCKER_COMPOSE = docker-compose

# Targets

## Build Docker containers
build:
    $(DOCKER_COMPOSE) build

## Start Docker containers in detached mode
up:
    $(DOCKER_COMPOSE) up -d

## Stop and remove Docker containers
down:
    $(DOCKER_COMPOSE) down

## View logs of Docker containers
logs:
    $(DOCKER_COMPOSE) logs -f

## Run tests (example target, replace with actual test commands)
test:
    @echo "Running tests..."
    # Add your test commands here

.PHONY: build up down logs test
