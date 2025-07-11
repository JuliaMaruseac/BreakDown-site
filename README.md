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

The frontend expects the backend on `http://localhost:8000`.

