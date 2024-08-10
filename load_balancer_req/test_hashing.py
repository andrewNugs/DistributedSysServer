from consistent_hashing import ConsistentHashing

def main():
    ch = ConsistentHashing()
    ch.add_server("server1")
    ch.add_server("server2")
    ch.add_server("server3")

    ch.print_hash_ring()

if __name__ == "__main__":
    main()
