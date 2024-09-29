from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/notify', methods=['POST'])
def send_notification():
    notification_data = request.get_json()
    # Simulate sending notification (e.g., SMS, Email)
    print(f"Sending notification to {notification_data['recipient']}: {notification_data['message']}")
    return jsonify({'status': 'Notification sent'}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
