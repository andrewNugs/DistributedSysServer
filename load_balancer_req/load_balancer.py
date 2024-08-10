from flask import Flask, request, jsonify
import requests
from consistent_hashing import ConsistentHashing
import os
import uuid

app = Flask(__name__)

# Initialize Consistent Hashing
N = 3  # Number of replicas required
ch = ConsistentHashing(replicas=3)

# Initialize servers (replace with your server setup)
servers = {
    "server1": "http://server1:5000",
    "server2": "http://server2:5000",
    "server3": "http://server3:5000"
}

# Add servers to the hash ring
for server_id in servers:
    ch.add_server(server_id)

@app.route('/rep', methods=['GET'])
def get_replicas():
    """Returns the number of replicas and a list of server replicas."""
    # Get the list of server IDs
    server_ids = list(servers.keys())

    # Construct the response JSON
    response = {
        "message": {
            "N": len(server_ids),
            "replicas": server_ids
        },
        "status": "successful"
    }

    # Return the response as JSON with a 200 status code
    return jsonify(response), 200

@app.route('/add', methods=['POST'])
def add_server():
    """Adds a new server instance."""
    data = request.get_json()
    server_id = data.get('server_id')
    server_url = data.get('server_url')
    
    if server_id and server_url:
        servers[server_id] = server_url
        ch.add_server(server_id)
        return jsonify({"message": f"{server_id} added."}), 201
    return jsonify({"message": "Invalid data."}), 400

@app.route('/rm', methods=['DELETE'])
def remove_server():
    """Removes a server instance."""
    data = request.get_json()
    server_id = data.get('server_id')
    
    if server_id in servers:
        del servers[server_id]
        ch.remove_server(server_id)
        return jsonify({"message": f"Server {server_id} removed."}), 200
    return jsonify({"message": "Server not found."}), 404

@app.route('/<path:path>', methods=['GET'])
def route_request2(path):
    """Routes the request to the appropriate server."""
    request_id = path
    server_id = ch.get_server(request_id)
    if not server_id or server_id not in servers:
        return jsonify({"message": "Server not available."}), 503
    
    server_url = servers[server_id]
    try:
        # Forward the request to the selected server
        response = requests.get(f"{server_url}/{path}")
        return jsonify(response.json()), response.status_code
    except requests.RequestException:
        return jsonify({"message": "Failed to route request."}), 503

@app.route('/test', methods=['GET'])
def route_request():
    request_id = str(uuid.uuid4())  # Generate a unique identifier for each request
    server_id = ch.get_server(request_id)
    
    if not server_id or server_id not in servers:
        return jsonify({"message": "Server not available."}), 503
    
    server_url = servers[server_id]
    try:
        response = requests.get(f"{server_url}/home")
        return jsonify(response.json()), response.status_code
    except requests.RequestException:
        return jsonify({"message": "Failed to route request."}), 503


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
