from sqlalchemy import Column, Integer, String
from lol.config import Base #calling Base from config.py module we created

#creating model or table in our database

#defining a table named champions

class Champion(Base):
    __tablename__ = "champions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    resource = Column(String(20))