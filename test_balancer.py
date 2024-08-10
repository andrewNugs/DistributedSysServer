import requests
import matplotlib.pyplot as plt

# URL of your load balancer
load_balancer_url = "http://localhost:5000/test"

# Number of requests to send
num_requests = 1000

# Dictionary to keep track of which server handled each request
load_distribution = {"server1": 0, "server2": 0, "server3": 0}

print(f"Sending {num_requests} requests to {load_balancer_url}\n")

for i in range(num_requests):
    response = requests.get(load_balancer_url)
    
    if response.status_code == 200:
        # Parse JSON response to get the server name
        json_response = response.json()
        server_name = json_response["message"].split(":")[1].strip()
        server_key = f"server{server_name}"
        
        if server_key in load_distribution:
            load_distribution[server_key] += 1
        else:
            print(f"Unexpected server name '{server_name}' in response: {response.text}")
    else:
        print(f"Request {i+1} failed with status code {response.status_code}")

# Print the load distribution results
print("\nLoad distribution among servers:")
for server, count in load_distribution.items():
    print(f"{server}: {count} requests")

# Plotting the results
servers = list(load_distribution.keys())
counts = list(load_distribution.values())

plt.figure(figsize=(10, 6))
plt.bar(servers, counts, color='skyblue')
plt.xlabel('Servers')
plt.ylabel('Number of Requests')
plt.title('Load Distribution Among Servers')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot to a file
plt.savefig('load_distribution.png')
