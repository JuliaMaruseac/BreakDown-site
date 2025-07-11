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

# Build the production bundle
npm run build
```

The frontend expects the backend on `http://localhost:8000`.

## Deploying with Docker

Railway will detect the `Dockerfile` and build the project automatically. You
can also build and run it locally:

```bash
docker build -t breakdown .
docker run -p 8000:8000 breakdown
```

The Dockerfile builds the React app and then starts the FastAPI server with
`uvicorn`.
