class ConsistentHashing:
    def _init_(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, key):
        hash_value = hash(key)
        return self.nodes[hash_value % len(self.nodes)]