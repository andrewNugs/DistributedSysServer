from consistent_hashing2 import ConsistentHashing
import requests
import time

def test_hash_functions():
    ch = ConsistentHashing(replicas=9, slots=512)
    ch.add_server("server1")
    ch.add_server("server2")
    ch.add_server("server3")

    test_requests = [f"request_{i}" for i in range(10000)]
    start_time = time.time()

    server_counts = {"server1": 0, "server2": 0, "server3": 0}

    for req in test_requests:
        server = ch.get_server(req)
        server_counts[server] += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Server counts: {server_counts}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    test_hash_functions()
