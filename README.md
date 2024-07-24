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
  ![Screenshot 2024-07-24 163714](https://github.com/user-attachments/assets/fd2987a1-8072-4a9f-9088-7b78fced9abc)


## Load Balancer Performance Analysis
A1: Load Distribution Among 3 Servers
In this experiment, we launched 10,000 async requests on 3 server containers and measured the request count handled by each server instance. The results are shown in the bar chart below:

![image](https://github.com/user-attachments/assets/ac277aaf-75b0-4c82-9246-ce8cee839479)

Observations:
Server 1:
Handles the highest number of requests, approximately 2000.
This indicates that Server 1 is receiving the majority of the load.
Server 2:
Handles the second highest number of requests, around 1800.
This shows that Server 2 is also significantly loaded but less than Server 1.
Server 3:
Handles the fewest requests, roughly 1200.
This suggests that Server 3 is underutilized compared to the other two servers.

A2: Scalability with Incrementing Servers N from 2 to 6
In this experiment, we increased the number of servers (N) from 2 to 6, launching 10,000 requests at each increment. We then measured and reported the average server load for each run in the line chart below.

![image](https://github.com/user-attachments/assets/cc30d2bd-a0c8-4f97-aa3d-0ea844d1bdc2)

Observations:
General Trend:

As the number of servers increases from 2 to 6, the average load on each server decreases.
**Specific Data Points:**

-N2: The average load is slightly above 5000.

-N3: The average load decreases to around 4000.

-N4: The average load further decreases to approximately 2000.

-N5: The load continues to drop slightly below 2000.

-N6: The average load is slightly above 1000.

Analysis:

**Load Distribution:**

The chart indicates that as more servers are added, the load is more evenly distributed, resulting in a lower average load per server. This is expected behavior in a well-functioning load-balanced system.

Scalability:

The system demonstrates good scalability, with the load on each server decreasing as more servers are added. This suggests that the load balancer effectively distributes requests across multiple servers.


- The load balancer efficiently distributes requests using consistent hashing.
- Docker ensures isolated environments for each server instance, making it easy to scale horizontally.
