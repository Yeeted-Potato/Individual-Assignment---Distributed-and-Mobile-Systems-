from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from database import Base, engine, get_db
from sqlalchemy.orm import Session
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

#@app.get("/customers/{customer_id}")
#def get_customer(customer_id: int):
#    return {"You asked for customer": customer_id}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

#give all customers in the database
@app.get("/customers")
def list_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

@app.post("/customers")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = models.Customer(name=customer.name, email=customer.email)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

    
