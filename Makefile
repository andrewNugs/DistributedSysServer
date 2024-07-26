.PHONY: build up down logs restart prune ps docker-ps compose-ps network network-inspect container-logs

# Build the Docker containers without using the cache to ensure a fresh build
build:
	sudo docker-compose build --no-cache

# Start the Docker containers in detached mode for background execution
up:
	sudo docker-compose up -d

# Stop and remove all running Docker containers and their networks
down:
	sudo docker-compose down

# Display logs from the running Docker containers for troubleshooting
logs:
	sudo docker-compose logs

# Restart the Docker service to apply any configuration changes
restart:
	sudo systemctl restart docker

# Clean up unused containers, networks, images, and optionally volumes to free up space
prune:
	sudo docker system prune -a -f

# List all currently running Docker containers to see their statuses
ps:
	sudo docker ps

# Show the status of containers managed by docker-compose
compose-ps:
	sudo docker-compose ps

# List all available Docker networks in the system
network:
	sudo docker network ls

# Inspect a specified Docker network to view its details
network-inspect:
	@echo "Usage: make network-inspect NETWORK=<network_name>"
	@[ -z "$(NETWORK)" ] && echo "Error: NETWORK variable is not set" && exit 1 || sudo docker network inspect $(NETWORK)

# Display logs for a specific container for detailed analysis
container-logs:
	@echo "Usage: make container-logs CONTAINER=<container_name>"
	@[ -z "$(CONTAINER)" ] && echo "Error: CONTAINER variable is not set" && exit 1 || sudo docker logs $(CONTAINER)
