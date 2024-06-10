from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        data = request.json
        return {"status": "Data received", "data": data}, 200
    else:
        return {"status": "Send some data!"}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
