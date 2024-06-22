# Customizable Load Balancer

This project implements a customizable load balancer that routes requests coming from several clients asynchronously among several servers to ensure an even load distribution.


## Introduction

This project includes a load balancer implemented using Flask and multiple server instances managed using Docker. The load balancer uses consistent hashing to distribute incoming requests among the server instances.

## Features

- Distributes requests evenly among servers using consistent hashing.
- Handles both GET and POST requests.
- Includes health check endpoints for monitoring server status.
- Easily scalable by adding more server instances.

## Setup

### Prerequisites

- Windows Subsystem for Linux (WSL)
- Ubuntu 20.04 or above
- Docker 20.10.23 or above
- Docker Compose 2.15.1 or above
- Python 3.8 or above

### Installing WSL and Ubuntu

1. **Enable WSL:**

    Open PowerShell as Administrator and run:

    ```powershell
    wsl --install
    ```

    Restart your computer if prompted.

2. **Install Ubuntu for WSL:**

    Open Microsoft Store, search for "Ubuntu", and install it. Alternatively, you can install it via PowerShell:

    ```powershell
    wsl --install -d Ubuntu-20.04
    ```

3. **Set WSL Version to 2:**

    Ensure WSL is set to version 2:

    ```powershell
    wsl --set-default-version 2
    ```

4. **Start Ubuntu:**

    Launch Ubuntu from the Start menu and complete the initial setup.

5. **Update and Upgrade Ubuntu:**

    Inside the Ubuntu terminal, run:

    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

### Project Setup

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

## Usage

Once the Docker containers are up and running, you can interact with the load balancer via the following endpoints:

- **Load Balancer API Endpoint:**
  - `http://localhost:5000/api`
  - Supports both GET and POST requests.
  - Forwards requests to one of the servers based on consistent hashing.

- **Server Endpoints:**
  - `http://localhost:5001/data`
  - `http://localhost:5002/data`
  - `http://localhost:5003/data`
  - Servers will respond based on the load balancer's distribution.

## Files

- `server.py`: Contains the code for the server instances.
- `consistent_hashing.py`: Contains the consistent hashing implementation.
- `load_balancer.py`: Contains the code for the load balancer.
- `Dockerfile`: Dockerfile for the load balancer.
- `Dockerfile_server`: Dockerfile for the server instances.
- `docker-compose.yml`: Docker Compose configuration to set up the services.

## Design Choices

- Used Flask for simplicity in setting up HTTP endpoints.
- Implemented consistent hashing to evenly distribute requests among servers.
- Used Docker Compose to manage multiple containers and networking.

## Assumptions

- The server instances are identical and stateless.
- The load balancer and servers are running in the same Docker network.
- The client IP is used as the key for consistent hashing.

## Testing

- Manually tested the load balancer by sending GET and POST requests using tools like `curl` and Postman.
- Verified that requests are distributed evenly among the servers.

## Performance Analysis

- The load balancer efficiently distributes requests using consistent hashing.
- Docker ensures isolated environments for each server instance, making it easy to scale horizontally.
