from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from lol.config import get_db
from lol.config import engine
from lol import crud, model

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#create tables, call before running app 
model.Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def lol(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/champions/")
def read_data(db: Session = Depends(get_db)):
    #Depends creates unique session for each request to avoid conn leaks
    champions = crud.get_champ(db)
    return champions

@app.post("/champions/")
def create_champ(name:str, resource:str, db: Session = Depends(get_db)):
    db_champ = crud.create_champ(db, name, resource)
    return db_champ


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    



