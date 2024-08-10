import hashlib
from bisect import bisect_right

class ConsistentHashing:
    def __init__(self, replicas: int = 9, slots: int = 512):
        self.replicas = replicas  # Number of virtual servers (K)
        self.slots = slots  # Total number of slots in the hash map (#slots)
        self.hash_ring = [None] * self.slots  # Initialize the consistent hash map
        self.server_map = {}  # Maps server names to their positions in the hash ring
        self.occupied_slots = []  # Sorted list of occupied slots for binary search

    def hash_request(self, request_id: str) -> int:
        """Hash function for request mapping (H(i))"""
        request_hash = int(hashlib.md5(request_id.encode()).hexdigest(), 16)
        return request_hash % self.slots

    def hash_virtual_server(self, server_id: str, replica_index: int) -> int:
        """Hash function for virtual server mapping (Φ(i, j))"""
        server_hash = int(hashlib.md5(f"{server_id}:{replica_index}".encode()).hexdigest(), 16)
        return server_hash % self.slots

    def add_server(self, server_id: str):
        """Adds a server and its replicas to the consistent hash map."""
        self.server_map[server_id] = []
        for i in range(self.replicas):
            position = self.hash_virtual_server(server_id, i)
            if self.hash_ring[position] is None:
                self.server_map[server_id].append(position)
                self.hash_ring[position] = server_id
                self.occupied_slots.append(position)
        self.occupied_slots.sort()

    def remove_server(self, server_id: str):
        """Removes a server and its replicas from the consistent hash map."""
        if server_id not in self.server_map:
            return
        for position in self.server_map[server_id]:
            self.hash_ring[position] = None
            self.occupied_slots.remove(position)
        del self.server_map[server_id]

    def get_server(self, request_id: str) -> str:
        """Maps a request to the appropriate server."""
        if not self.occupied_slots:
            raise Exception("No available servers in the hash ring")
        
        position = self.hash_request(request_id)
        
        # Find the nearest server using binary search
        index = bisect_right(self.occupied_slots, position)
        if index == len(self.occupied_slots):
            index = 0  # Wrap around to the first slot
        
        return self.hash_ring[self.occupied_slots[index]]

    def print_hash_ring(self):
        """Prints the current state of the hash ring."""
        for i in range(self.slots):
            print(f"Slot {i}: {self.hash_ring[i]}")
