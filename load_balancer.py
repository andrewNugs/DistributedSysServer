from flask import Flask, request, jsonify
import requests
from consistent_hashing import ConsistentHashing

app = Flask(_name_)
hash_ring = ConsistentHashing()

# Dummy list of servers (Replace these with your actual server IPs or DNS names)
servers = ["http://server1:5001", "http://server2:5002", "http://server3:5003"]
for server in servers:
    hash_ring.add_node(server)

@app.route('/api', methods=['GET', 'POST'])
def distribute_request():
    key = request.remote_addr  # Example: use the client IP as the key for consistent hashing
    server_url = hash_ring.get_node(key)

    if request.method == 'POST':
        # Forward the POST request to the correct server
        response = requests.post(f"{server_url}/data", json=request.json)
        return jsonify({"message": "Request forwarded", "server": server_url, "response": response.json()}), response.status_code
        else:
        # Forward the GET request to the correct server
        response = requests.get(f"{server_url}/data")
        return jsonify({"message": "Request forwarded", "server": server_url, "response": response.json()}), response.status_code >

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)