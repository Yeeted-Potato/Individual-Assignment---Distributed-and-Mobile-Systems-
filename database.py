#get access to tools from the sqlalchemy library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#store url of database from order.db file in a variable
SQLalchemy_database_url = "sqlite:///./orders.db"

#create engine object to connect to our database
engine = create_engine(
    SQLalchemy_database_url, 
    connect_args={"check_same_thread": False}
)

#Creates sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#parent class 
Base = declarative_base()

#Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()