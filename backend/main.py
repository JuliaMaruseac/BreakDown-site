from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

class Case(BaseModel):
    id: int
    date: str
    driver: str
    company: Optional[str] = None
    truck: Optional[str] = None
    truck_owner: Optional[str] = None
    trailer: Optional[str] = None
    trailer_owner: Optional[str] = None
    location: Optional[str] = None
    problem: Optional[str] = None
    cost: Optional[str] = None
    payment: Optional[str] = None
    solution: Optional[str] = None
    status: Optional[str] = None
    culprit: Optional[str] = None
    efs_code: Optional[str] = None
    media: List[str] = []
    invoice: Optional[str] = None

cases_db: List[Case] = []

@app.post('/cases', response_model=Case)
async def create_case(
    date: str = Form(...),
    driver: str = Form(...),
    company: Optional[str] = Form(None),
    truck: Optional[str] = Form(None),
    truck_owner: Optional[str] = Form(None),
    trailer: Optional[str] = Form(None),
    trailer_owner: Optional[str] = Form(None),
    location: Optional[str] = Form(None),
    problem: Optional[str] = Form(None),
    cost: Optional[str] = Form(None),
    payment: Optional[str] = Form(None),
    solution: Optional[str] = Form(None),
    status: Optional[str] = Form(None),
    culprit: Optional[str] = Form(None),
    efs_code: Optional[str] = Form(None),
    media_files: List[UploadFile] = File([]),
    invoice_file: Optional[UploadFile] = File(None)
):
    cid = len(cases_db) + 1
    media_paths = []
    for f in media_files:

        path = os.path.join(UPLOAD_DIR, f'{cid}_{f.filename}')
        filename = os.path.basename(f.filename)
        path = os.path.join(UPLOAD_DIR, f"{cid}_{filename}")
        with open(path, 'wb') as out:
            out.write(await f.read())
        media_paths.append(path)

    invoice_path = None
    if invoice_file:
        invoice_path = os.path.join(UPLOAD_DIR, f'{cid}_inv_{invoice_file.filename}')
        inv_filename = os.path.basename(invoice_file.filename)
        invoice_path = os.path.join(UPLOAD_DIR, f"{cid}_inv_{inv_filename}")
        with open(invoice_path, 'wb') as out:
            out.write(await invoice_file.read())

    case = Case(
        id=cid,
        date=date,
        driver=driver,
        company=company,
        truck=truck,
        truck_owner=truck_owner,
        trailer=trailer,
        trailer_owner=trailer_owner,
        location=location,
        problem=problem,
        cost=cost,
        payment=payment,
        solution=solution,
        status=status,
        culprit=culprit,
        efs_code=efs_code,
        media=media_paths,
        invoice=invoice_path
    )
    cases_db.append(case)
    return case

@app.get('/cases', response_model=List[Case])
async def get_cases():
    return cases_db

# Serve the built React app if it exists
FRONTEND_DIST = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist')
if os.path.isdir(FRONTEND_DIST):
    app.mount('/', StaticFiles(directory=FRONTEND_DIST, html=True), name='frontend')
    app.mount('/uploads', StaticFiles(directory=UPLOAD_DIR), name='uploads')
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
