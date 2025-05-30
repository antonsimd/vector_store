from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """
    Health check endpoint to verify the API is running
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'service': 'Flask API',
        'version': '1.0.0'
    }), 200

@app.route('/', methods=['GET'])
def root():
    """
    Root endpoint with basic API information
    """
    return jsonify({
        'message': 'Welcome to the Flask API',
        'endpoints': [
            {'path': '/', 'method': 'GET', 'description': 'API information'},
            {'path': '/health', 'method': 'GET', 'description': 'Health check'}
        ]
    }), 200

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5001))
    # Get debug mode from environment variable or default to True for development
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug) 