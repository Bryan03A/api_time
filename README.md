# Time API

A simple REST API that returns the current time in the specified timezone.

## Features

- Returns current time in a readable format
- Configurable timezone (default: America/Guayaquil)
- CORS enabled
- Automated testing with GitHub Actions
- Automated deployment to Render

## Requirements

- Python 3.10+
- Flask
- flask-cors
- pytz

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

```bash
python app.py
```

The API will be available at `http://localhost:5000/api/time`

## API Endpoints

### Get Current Time

```
GET /api/time
```

**Response:**
```json
{
  "message": "Current time fetched successfully.",
  "formatted_time": "25/05/2025 11:48:27 PM"
}
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment:

1. **Test and Deploy Workflow** (`python-test.yml`):
   - Runs on every push to main/master and pull requests
   - Verifies the app can be imported
   - Runs linter (flake8)

2. **Deploy Workflow** (`deploy.yml`):
   - Triggers after successful test workflow
   - Deploys to Render automatically

## Deployment to Render

### Manual Deployment
1. Push your code to a GitHub repository
2. Create a new Web Service on Render
3. Connect your repository
4. Render will automatically detect the Python app
5. Click "Create Web Service"

### Automatic Deployment (Recommended)
1. Create a new Web Service on Render manually the first time
2. In your GitHub repository, go to Settings > Secrets > Actions
3. Add the following secrets:
   - `RENDER_API_KEY`: Your Render API key
   - `RENDER_SERVICE_ID`: Your Render service ID (find it in the Render dashboard)

After setting up the secrets, every push to main/master will trigger an automatic deployment if tests pass.

## Configuration

No environment variables are required for basic usage. The default timezone is set to 'America/Guayaquil'.

## License

MIT