
# JWT Authentication Project

## Overview
This project demonstrates a simple authentication system using JWT (JSON Web Tokens). It consists of a backend server for authentication and a client application to interact with the server.

## Project Structure
```
jwt-auth-client/
|-- public/
|   |-- index.html
|   |-- app.js
|-- server/
|   |-- server.js
|-- Dockerfile
|-- package.json
jwt-auth-server/
|-- app.py
|-- Dockerfile
|-- requirements.txt
```

## Prerequisites
- Docker
- Docker Compose
- Node.js (for local development)
- Python

## Environment Variables
Create a `.env` file in the root directory with the following variables:

```
SECRET_KEY=your_secret_key
JWT_USER=test_user
JWT_PASS=test_password
LOG_LEVEL=DEBUG
JWT_EXPIRATION_MINUTES=30
FLASK_DEBUG=True
PORT=5000
```

## Setup and Running the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/nate-marshall/jwt-hello-world.git
cd jwt-hello-world
```

### Step 2: Build and Run the Docker Containers
Make sure you're in the root directory where `docker-compose.yml` is located.
```bash
docker-compose up --build
```

### Step 3: Access the Applications
- **Client Application:** [http://localhost:8000](http://localhost:8000)
- **Server Application:** [http://localhost:5000](http://localhost:5000)

## API Endpoints

### POST /login
Authenticate the user and get a JWT.

**Request:**
```json
{
  "username": "test_user",
  "password": "test_password"
}
```

**Response:**
```json
{
  "token": "<jwt_token>"
}
```

### GET /protected
Access a protected resource using the JWT.

**Request Headers:**
```
Authorization: Bearer <jwt_token>
```

**Response:**
```json
{
  "message": "Welcome <user>"
}
```

## Running the Client Application Locally

### Step 1: Install Dependencies
```bash
cd jwt-auth-client
npm install
```

### Step 2: Start the Client Application
```bash
npm start
```

The client application will be available at [http://localhost:8000](http://localhost:8000).

## Running the Server Application Locally

### Step 1: Create and Activate a Virtual Environment
```bash
cd jwt-auth-server
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Start the Server Application
```bash
python app.py
```

The server application will be available at [http://localhost:5000](http://localhost:5000).

## Example Curl Command

To test the login endpoint, you can use the following curl command:
```bash
curl --location 'http://127.0.0.1:8000/login' --header 'Content-Type: application/json' --data '{
    "username": "test_user",
    "password": "test_password"
}'
```

## Important Notes
- Ensure that the environment variables are correctly set up.
- This project is intended for educational purposes and should not be used in production without proper security measures.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Flask for the server framework.
- Node.js and Express for the client server.
- Docker and Docker Compose for containerization.
