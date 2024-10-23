from sqlalchemy.orm import Session
from lol.model import Champion


def get_champ(db:Session):
    return db.query(Champion).all() #creates query for all data in Champion


def create_champ(db: Session, name:str, resource:str):
    db_champ = Champion(name=name, resource=resource)
    db.add(db_champ)
    db.commit()
    db.refresh(db_champ)
    return db_champ

def get_champ_name(db:Session, name:str):
    return db.query(Champion).filter(Champion.name==name).first()
