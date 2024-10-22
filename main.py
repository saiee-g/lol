from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from lol.config import get_db
from lol.config import engine
from lol import crud, model

app = FastAPI()

#create tables, call before running app 
model.Base.metadata.create_all(bind=engine)

@app.get("/")
def lol():
    return "League of Legends Champions, go to /champions/"

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
    



