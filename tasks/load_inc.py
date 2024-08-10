import requests
import matplotlib.pyplot as plt
import numpy as np
import time

# List of server counts to test
server_counts = [2, 3, 4, 5, 6]
num_requests = 10000
base_url = 'http://localhost:5000/test'  # Updated to match endpoint

def send_requests_and_get_load(num_servers):
    urls = [f"{base_url}/{i}" for i in range(num_servers)]
    load = [0] * num_servers
    
    print(f"Sending {num_requests} requests to {base_url} with {num_servers} servers...")
    start_time = time.time()
    
    for i in range(num_requests):
        url = urls[i % num_servers]
        requests.get(url)
        load[i % num_servers] += 1
    
    end_time = time.time()
    print(f"Requests sent. Time taken: {end_time - start_time:.2f} seconds")
    
    return np.array(load)

def main():
    avg_loads = []

    for num_servers in server_counts:
        print(f"Testing with {num_servers} servers...")
        
        # Send requests and get load distribution
        loads = send_requests_and_get_load(num_servers)
        avg_load = np.mean(loads)
        avg_loads.append(avg_load)
        
        # Optional: Print the load for each server for debugging
        print(f"Load distribution for {num_servers} servers: {loads}")
        print(f"Average load: {avg_load}")

    # Plot the results
    print("Beginning plotting...")
    plt.figure(figsize=(10, 6))
    plt.plot(server_counts, avg_loads, marker='o', linestyle='-', color='b')
    plt.xlabel('Number of Servers')
    plt.ylabel('Average Load')
    plt.title('Average Load per Server vs Number of Servers')
    plt.xticks(server_counts)
    plt.grid(True)
    plt.savefig('average_load_vs_servers.png')
    print("Graph plotted as 'average_load_vs_servers.png'")

if __name__ == "__main__":
    main()
