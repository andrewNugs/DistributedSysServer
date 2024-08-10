import asyncio
import aiohttp
from collections import Counter
import json

LOAD_BALANCER_URL = 'http://localhost:5000/home'
TOTAL_REQUESTS = 10000

async def fetch(session):
    async with session.get(LOAD_BALANCER_URL) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch(session)) for _ in range(TOTAL_REQUESTS)]
        responses = await asyncio.gather(*tasks)
    
    # Extract server IDs from responses
    server_ids = [json.loads(response)['message']['server_id'] for response in responses]
    
    # Count occurrences
    count = Counter(server_ids)
    
    # Save counts to a JSON file
    with open('request_counts.json', 'w') as f:
        json.dump(count, f)

    print("Request distribution:", count)

if __name__ == '__main__':
    asyncio.run(main())
