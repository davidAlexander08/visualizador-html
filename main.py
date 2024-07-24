from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/view", response_class=HTMLResponse)
async def view_html(file_path: str = Query(..., description="Path to the HTML file")):
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Arquivo nao encontrado, provavelmente foi fornecido o caminho errado")

    with open(file_path, "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
