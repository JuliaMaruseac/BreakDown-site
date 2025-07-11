# BreakDown Site

This repository contains a simple FastAPI backend and React frontend to track case reports.

## Backend

Run the backend with Python:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Uploaded files are stored in `backend/uploads`.

## Frontend

Install dependencies and run the development server:

```bash
cd frontend
npm install
npm run start
```

The frontend communicates with the backend using relative paths, so it works as long as both are served from the same origin (for example when running locally on `http://localhost:8000` or when deployed together on Railway).

## Deploying with Nixpacks

This repository contains both a Python backend and a Node frontend.  A
`nixpacks.toml` configuration is included so that Railway (or any system that
uses Nixpacks) can build the project:

1. Python dependencies are installed from `backend/requirements.txt`.
2. Frontend dependencies are installed and the React app is built.
3. The FastAPI server is started with `uvicorn`.

Simply run `nixpacks build` or deploy on Railway and the build plan will be
picked up automatically.

The `nixpacks.toml` file installs Node.js 18 and Python 3.11. Ensure all build
tools such as Webpack and Babel are listed in `frontend/package.json` so the
React app can compile during deployment.
