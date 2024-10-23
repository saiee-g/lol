from fastapi import FastAPI, Depends, Request, Form
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from lol.config import get_db
from lol.config import engine
from lol import crud, model

app = FastAPI()

app.mount("/static", StaticFiles(directory="lol/static"), name="static")
templates = Jinja2Templates(directory="lol/templates")

#create tables, call before running app 
model.Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def lol(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
    # try:
    #     return templates.TemplateResponse(request=request, name="index.html")
    # except Exception as error:
    #     return HTMLResponse(content=str(error), status_code=500)

@app.get("/champions/", response_class=HTMLResponse)
def read_data(request: Request, db: Session = Depends(get_db)):
    #Depends creates unique session for each request to avoid conn leaks
    champions = crud.get_champ(db)
    print(champions)
    return templates.TemplateResponse(
        "champ_list.html", {"request": request, "champions": champions}
    )

@app.get("/champions/", response_class=HTMLResponse)
def read_data(request: Request, db: Session = Depends(get_db)):
    #Depends creates unique session for each request to avoid conn leaks
    champions = crud.get_champ(db)
    print(champions)
    return templates.TemplateResponse(
        "champ_list.html", {"request": request, "champions": champions}
    )

@app.get("/champions/{name}")
def find_champ(name:str, db: Session = Depends(get_db)):
    existing_champ = crud.get_champ_name(db,name)
    if existing_champ:
        found_champ = crud.get_champ_name(db, name)
        return found_champ
    else:
        raise HTTPException(status_code=404, detail="Champion not found")

@app.post("/champions/")
def create_champ(request:Request, name:str = Form(...), resource:str = Form(...), db: Session = Depends(get_db)):
    existing_champ = crud.get_champ_name(db, name)
    if existing_champ:
        raise HTTPException(status_code=400, detail="Champion already exists")
    db_champ = crud.create_champ(db, name, resource)
    return db_champ

@app.delete("/champions/")
def delete_champ(name:str, db:Session = Depends(get_db)):
    existing_champ = crud.get_champ_name(db,name)
    if existing_champ:
        deleted_champ = crud.delete_champ(db, name)
        return {"response" : "deleted successfully", "champion" : name}
    else:
        raise HTTPException(status_code=404, detail="Champion not found")
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    



