from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory queue
message_queue = []

@app.route('/produce', methods=['POST'])
def produce():
    """Adds a message to the queue."""
    data = request.json
    if 'message' not in data:
        return jsonify({"error": "Message is required"}), 400
    message_queue.append(data['message'])
    return jsonify({"status": "Message added", "queue_size": len(message_queue)})

@app.route('/consume', methods=['GET'])
def consume():
    """Retrieves and removes a message from the queue."""
    if not message_queue:
        return jsonify({"error": "Queue is empty"}), 404
    message = message_queue.pop(0)
    return jsonify({"message": message, "queue_size": len(message_queue)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)

