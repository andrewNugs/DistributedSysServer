import hashlib

class ConsistentHashing:
    def __init__(self, replicas: int = 9, slots: int = 512):
        self.replicas = replicas  # Number of virtual servers (K)
        self.slots = slots  # Total number of slots in the hash map (#slots)
        self.hash_ring = [None] * self.slots  # Initialize the consistent hash map
        self.server_map = {}  # Maps server names to their positions in the hash ring

    def hash_request(self, request_id: str) -> int:
        """Hash function for request mapping (H(i))"""
        request_hash = int(hashlib.sha256(request_id.encode()).hexdigest(), 16)
        return request_hash % self.slots

    def hash_virtual_server(self, server_id: str, replica_index: int) -> int:
        """Hash function for virtual server mapping (Φ(i, j))"""
        server_hash = int(hashlib.sha256(f"{server_id}:{replica_index}".encode()).hexdigest(), 16)
        return server_hash % self.slots

    def add_server(self, server_id: str):
        """Adds a server and its replicas to the consistent hash map."""
        self.server_map[server_id] = []
        for i in range(self.replicas):
            position = self.hash_virtual_server(server_id, i)
            self.server_map[server_id].append(position)
            self.hash_ring[position] = server_id

    def remove_server(self, server_id: str):
        """Removes a server and its replicas from the consistent hash map."""
        if server_id not in self.server_map:
            return
        for position in self.server_map[server_id]:
            self.hash_ring[position] = None
        del self.server_map[server_id]

    def get_server(self, request_id: str) -> str:
        """Maps a request to the appropriate server."""
        position = self.hash_request(request_id)
        
        # Move clockwise in the hash ring to find the next available server
        for i in range(self.slots):
            server = self.hash_ring[(position + i) % self.slots]
            if server is not None:
                return server
        
        raise Exception("No available servers in the hash ring")
