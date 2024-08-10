import requests

# URL of your load balancer
load_balancer_url = "http://localhost:5000/test"

# Number of requests to send
num_requests = 10000

# Dictionary to keep track of which server handled each request
load_distribution = {"server1": 0, "server2": 0, "server3": 0}

print(f"Sending {num_requests} requests to {load_balancer_url}\n")

for i in range(num_requests):
    response = requests.get(load_balancer_url)
    
    if response.status_code == 200:
        server_name = response.text.split(":")[1].strip()

        server_key = f"server{server_name}"
        if server_key in load_distribution:
            load_distribution[server_key] += 1
        else:
            print(f"Unexpected server name '{server_name}' in response: {response.text}")
    else:
        print(f"Request {i+1} failed with status code {response.status_code}")
        load_distribution[server_key] += 1

# Print the load distribution results
print("Load distribution among servers:")
for server, count in load_distribution.items():
    print(f"{server}: {count} requests")
