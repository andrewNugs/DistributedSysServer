import aiohttp
import asyncio
import matplotlib.pyplot as plt
from collections import Counter

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = "http://localhost:5000/test"  # Replace with your load balancer's URL
    num_requests = 10000
    
    # Print the initial message
    print(f"Sending {num_requests} requests to {url}")
    
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(num_requests):
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
    
    # Print message after sending requests
    print("All requests sent. Beginning plotting.")
    
    # Count how many times each server responded
    server_count = Counter(responses)
    
    # Plotting the results
    plt.bar(server_count.keys(), server_count.values())
    plt.xlabel('Server')
    plt.ylabel('Number of Requests Handled')
    plt.title('Request Distribution Across Servers')
    
    # Save the graph to a file
    plt.savefig('server_load_distribution.png')
    
    # Print final message
    print("Graph plotted and saved as 'server_load_distribution.png'")

if __name__ == '__main__':
    asyncio.run(main())
