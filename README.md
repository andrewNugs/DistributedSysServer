# Load Balancer Project
## Usage
### Prerequisites
- Docker Version 20.10.23 or above
- Python
- Docker compose
- Ubuntu 20.04 LTS or above	
### Docker Installation
Run the command to install Docker:
```bash
   sudo apt-get update
   sudo apt-get install ca-certificates curl gnupg lsb-release
   sudo mkdir -p /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Run this command to install Docker Compose:
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
1. **/rep endpoint `c`**
   ![/rep endpoint](screenshots/Screenshot(153).png)

3. **/home endpoint e.g for server at `http://localhost:5001/home` server1**
 ![/home endpoint](screenshots/Screenshot(154).png)

5. **/add endpoint**
Provide the n field and a list of hostnames e.g adding 4:
curl -X POST http://localhost:5000/add \
     -H "Content-Type: application/json" \
     -d '{"server_id": "server4", "server_url": "http://server4:5000"}'
 ![/add endpoint](screenshots/Screenshot(155).png)
6. **/remove endpoint**
Provide the n field and a list of hostnames e.g removing 4:
curl -X DELETE http://localhost:5000/rm \
     -H "Content-Type: application/json" \
     -d '{"server_id": "server4"}' 
![/rm endpoint](screenshots/Screenshot(156).png)
 
## Testing and Performance Analysis
#### Load Distribution Among 3 Servers
#### Observations
!(screenshots/Screenshot(151).png) 
#### Analysis
- The load distribution is uneven, with `server2` handling the most requests and `server3` handling the least.
- Possible reasons for this discrepancy could include the network latency, or environmental factors.

**Scalability with Incrementing Servers N from 2 to 6**
#### Observations
 !(screenshots/Screenshot(152).png)
#### Analysis
- The average load per server decreases as the number of servers increases.
- The load balancer scales efficiently with more servers.

#### Load Balancer Recovery from Server Failure
#### Observations
!(screenshots/Screenshot(149).png)
 

#### Observations:
-The load balancer would switch them all off and start a new server instance.
**A-4 Finally, modify the hash functions H(i), Φ(i, j) and report the observations from (A-1) and (A-2). **
#### Load Distribution Among 3 Servers with modified hash functions H(i), Φ(i, j). 
#### Observations
!(screenshots/Screenshot(150).png)
-As seen in the video, the loads were more fairly distributed than the others.
