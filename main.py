from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/view", response_class=HTMLResponse)
async def view_html(file_path: str = Query(..., description="Path to the HTML file")):
    # Sanitize the file_path to avoid directory traversal attacks
    #file_path = os.path.normpath(file_path)  # Normalize the path
    print(f"Received file_path: {file_path}")
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Read and return the file content
    with open(file_path, "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)
    
