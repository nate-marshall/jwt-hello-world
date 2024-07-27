from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import os
import logging
from dotenv import load_dotenv
import jwt  # Import PyJWT

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
JWT_USER = os.getenv('JWT_USER')
JWT_PASS = os.getenv('JWT_PASS')
JWT_EXPIRATION_MINUTES = int(os.getenv('JWT_EXPIRATION_MINUTES', 30))
DEBUG_MODE = os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1', 't']

# Configure logging
log_level = os.getenv('LOG_LEVEL', 'DEBUG').split('#')[0].strip().upper()
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

# Route to generate JWT
@app.route('/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    logger.debug("Received login data")

    if 'username' not in auth_data or 'password' not in auth_data:
        logger.warning("Missing username or password in request")
        return jsonify({'message': 'Missing username or password'}), 400

    if auth_data['username'] == JWT_USER and auth_data['password'] == JWT_PASS:
        token = jwt.encode({
            'user': auth_data['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRATION_MINUTES)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        logger.info(f"Generated token for user: {auth_data['username']}")
        return jsonify({'token': token})
    else:
        logger.warning(f"Invalid login attempt for user: {auth_data['username']}")
        return jsonify({'message': 'Invalid credentials'}), 401

# Route to verify JWT
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization').split()[1]
    logger.debug("Received token")

    if not token:
        logger.warning("Token is missing in request")
        return jsonify({'message': 'Token is missing'}), 403
    
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        logger.info(f"Token verified for user: {data['user']}")
        return jsonify({'message': f'Access granted', 'user': data['user']})
    except jwt.ExpiredSignatureError:
        logger.error("Token has expired")
        return jsonify({'message': 'Token has expired'}), 403
    except jwt.InvalidTokenError as e:
        logger.error(f"Invalid token: {str(e)}")
        return jsonify({'message': 'Invalid token'}), 403

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=DEBUG_MODE, host='127.0.0.1', port=5000)
