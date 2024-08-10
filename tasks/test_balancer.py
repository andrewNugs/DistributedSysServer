import asyncio
import aiohttp

# Base URL of the load balancer
BASE_URL = 'http://localhost:5000/test'

async def send_request(session, request_id):
    params = {'request_id': request_id}
    async with session.get(BASE_URL, params=params) as response:
        result = await response.json()
        print(f"Request ID: {request_id}, Response: {result}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10000):
            request_id = f'request_{i}'  # Unique request_id for each request
            tasks.append(send_request(session, request_id))
        
        # Run all tasks concurrently
        await asyncio.gather(*tasks)

# Run the main function to execute the requests
if __name__ == '__main__':
    asyncio.run(main())
