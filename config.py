from sqlalchemy import create_engine # creates engine for db
from sqlalchemy.orm import sessionmaker #creates sessions for each query request
from sqlalchemy.ext.declarative import declarative_base #creates base class for all other models to inherit from

#DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"  #connection string, used to connect fastAPI with database
#postgresql://-->postgresql/which database),
#(user-->username of postgres),
#(password-->user's password),
#(localhost-->ip or hostname of server on which the db is)
#(5432-->default port for postgres)
#(mydatabase->db you want to conncet to)

DATABASE_URL = "postgresql://postgres:Saiee%40123@localhost:5432/lol"

engine = create_engine(DATABASE_URL) #create engine for the specified db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #creates session

Base = declarative_base() #Base class created

def get_db():   
    #whenever get_db is called, Sessionlocal is initialized. if db fails tp load it still closes the db due to finally
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


