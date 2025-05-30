# Simple Flask API with Health Check

A minimal Python Flask API that includes a health check endpoint for monitoring and basic API information.

## Features

- **Health Check Endpoint**: `/health` - Returns API status and timestamp
- **Root Endpoint**: `/` - Provides basic API information and available endpoints
- **JSON Responses**: All endpoints return structured JSON data
- **Environment Configuration**: Configurable port and debug mode via environment variables

## Setup and Installation

### 1. Activate Virtual Environment
Since you already have a virtual environment set up:

```bash
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

The API will start running on `http://localhost:5000` by default.

## API Endpoints

### GET /
Returns basic API information and available endpoints.

**Response:**
```json
{
  "message": "Welcome to the Flask API",
  "endpoints": [
    {"path": "/", "method": "GET", "description": "API information"},
    {"path": "/healthcheck", "method": "GET", "description": "Health check"}
  ]
}
```

### GET /health
Health check endpoint that returns the current status of the API.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000000",
  "service": "Flask API",
  "version": "1.0.0"
}
```

## Environment Variables

- `PORT`: Port number for the API (default: 5000)
- `DEBUG`: Enable/disable debug mode (default: True)

Example:
```bash
PORT=8080 DEBUG=False python app.py
```

## Testing

You can test the endpoints using curl:

```bash
# Test root endpoint
curl http://localhost:5000/

# Test health check
curl http://localhost:5000/health
```

Or open the URLs in your browser to see the JSON responses. 