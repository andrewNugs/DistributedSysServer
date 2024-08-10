import requests
import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np

load_balancer_url = 'http://localhost:5000/test'
num_requests = 10000
server_count = 3  # Initial number of server instances
check_interval = 5  # Interval to check server status in seconds

def send_requests():
    """Send a batch of requests to the load balancer."""
    print(f"Sending {num_requests} requests to {load_balancer_url}...")
    start_time = time.time()
    for _ in range(num_requests):
        requests.get(load_balancer_url)
    end_time = time.time()
    print(f"Requests sent. Time taken: {end_time - start_time:.2f} seconds")

def get_server_status():
    """Check the status of all server containers."""
    statuses = []
    for i in range(server_count):
        result = subprocess.run(
            ["docker", "ps", "-q", "--filter", f"name=server{i+1}"],
            capture_output=True, text=True
        )
        statuses.append(result.stdout.strip() != "")
    return statuses

def stop_server_instances():
    """Stop all server containers."""
    print("Stopping server instances...")
    for i in range(server_count):
        subprocess.run(["docker-compose", "stop", f"server{i+1}"])
        time.sleep(1)  # Small delay to ensure container stops properly

def start_server_instances():
    """Start all server containers."""
    print("Starting server instances...")
    for i in range(server_count):
        subprocess.run(["docker-compose", "start", f"server{i+1}"])
        time.sleep(1)  # Small delay to ensure container starts properly

def check_and_restart_servers():
    """Check server status and restart if needed."""
    while True:
        statuses = get_server_status()
        if all(statuses):
            print("All servers are up and running.")
            break
        else:
            print("Some servers are down. Restarting...")
            start_server_instances()
            time.sleep(check_interval)  # Wait before checking again

def plot_results(loads):
    """Plot the results of server loads."""
    plt.figure(figsize=(10, 6))
    plt.plot(loads, marker='o', linestyle='-', color='b')
    plt.xlabel('Request Batch')
    plt.ylabel('Server Load')
    plt.title('Server Load During Failures')
    plt.grid(True)
    plt.savefig('server_load_during_failures.png')
    print("Graph plotted as 'server_load_during_failures.png'")

def main():
    loads = []
    try:
        # Initial requests
        print("Beginning initial request batch...")
        send_requests()

        # Simulate server failures
        print("Simulating server failures...")
        stop_server_instances()
        time.sleep(30)  # Wait for some time to simulate failure
        
        # Restart servers and check status
        start_server_instances()
        print("Waiting for servers to restart...")
        check_and_restart_servers()

        # Send more requests to test recovery
        print("Beginning recovery request batch...")
        send_requests()

        # Collect load data (simulate collection here for demonstration purposes)
        # This should be replaced with actual data collection from your system
        loads.append(np.random.randint(100, 300))  # Placeholder value
        loads.append(np.random.randint(100, 300))  # Placeholder value

        plot_results(loads)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
