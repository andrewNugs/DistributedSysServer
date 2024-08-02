# Load Balancer Project

- **load_balancer_requirements/**: Contains load balancer files.
- **server_requirements/**: Contains server files.
- **code_test/**: Contains code to test the load balancer.
- **docker-compose.yml**: Defines Docker services.
- **Makefile**: Provides commands for Docker operations.
- **Flask**: Used to build the load balancer and server. It is a framework that is lightweight and easy-to-use. 
- **Consistent Hashing**: Implemented for server selection based on request characteristics, ensuring distribution of load to the servers.
- **Docker**: Ensures consistent deployment environments across different machines. 
- The containers are in the same network environment for efficient communication.

## Usage

### Prerequisites

- Docker Version 20.10.23 or above
- Python
- Docker compose
- Ubuntu 20.04 LTS or above

### Docker Installation

Run the following commands to install Docker:

```bash
   sudo apt-get update
   sudo apt-get install ca-certificates curl gnupg lsb-release
   sudo mkdir -p /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
```
To install Docker Compose:

```bash
   sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
### Building and Running

1. **Build Docker Images:**
```bash
   make build 
```
2. **Start Services:**
```bash
   make up
```
3. **Access Load Balancer**
- To check server replicas
```bash
    curl -X GET http://localhost:5000/rep
```
- To check heartbeat for server e.g. server1
```bash
    curl -X GET http://localhost:5001/heartbeat
```
- To add server e.g 3 servers
```bash
    curl -X POST http://localhost:5000/add     -H "Content-Type: application/json"     -d '{"n": 3}'
```
- To remove server e.g 1 server
```bash
   curl -X DELETE http://localhost:5000/rm     -H "Content-Type: application/json"     -d '{"n": 1}'
```
## Testing and Performance Analysis

1. **/rep endpoint `c`** 

![alt text](screenshot/image-1.png)

2. **/heartbeat endpoint e.g for server at `http://localhost:5002/hearbeat` server_2**

![alt text](screenshot/image-3.png)

3. **/home endpoint e.g for server at  `http://localhost:5001/home` server_1**

![alt text](screenshot/image-4.png)

4. **/add endpoint**
- provide the n field and a list of hostnames e.g adding 4:
``` bash
    curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{
    "n": 4,
    "hostnames": ["server_4", "server_5", "server_6", "server_7"]
}'
```
![alt text](screenshot/image-5.png)

- If no provide hostnames, they are generated automatically based on the number n e.g adding 3 servers:

``` bash
    curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{
    "n": 3
}'
```
![alt text](screenshot/image-6.png)

- To simulate an *error* where the n field is missing in the JSON payload:

``` bash
    curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{
    "hostnames": ["server_20", "server_21", "server_30"]
}'
```
![alt text](screenshot/image-7.png)

- confirm the replicas in the server after adding processes

![alt text](screenshot/image-8.png)

5. **/rem endpoint**
- provide the n field and a list of hostnames to remove e.g. server_1 and server_2:
``` bash
    curl -X DELETE http://localhost:5000/rm -H "Content-Type: application/json" -d '{
    "n": 2,
    "hostnames": ["server_1", "server_2"]
}'
```
![alt text](screenshot/image-9.png)

- No hostnames, they should be selected randomly to be removed e.g 3:
``` bash
    curl -X DELETE http://localhost:5000/rm -H "Content-Type: application/json" -d '{
    "n": 3
}'
```

- Simulate an *error* situation where the length of hostnames exceeds n:
``` bash
    curl -X DELETE http://localhost:5000/rm -H "Content-Type: application/json" -d '{
    "n": 2,
    "hostnames": ["server_5", "server_7", "server_8"]
}'

```
