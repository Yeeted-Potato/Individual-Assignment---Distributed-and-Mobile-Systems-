from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine
import models

app = FastAPI()

#create each table in the database
Base.metadata.create_all(bind=engine)

class CustomerCreate(BaseModel):
    name: str
    email: str
    
@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"You asked for customer": customer_id}

@app.post("/customers")
def create_customer(customer: CustomerCreate):
    return {"Recieved": customer.name, "email": customer.email}

    
