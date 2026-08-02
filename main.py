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
    
class OrderCreate(BaseModel):
    product: str
    quantity: int

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

#create a path for customers to create an order, match customer id and have columns of info for database
@app.post("/customers/{customer_id}/orders")
def create_order(customer_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    new_order = models.Order(
        customer_id=customer_id,
        product=order.product,
        quantity=order.quantity,
    )
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
    
#create a path to list orders for a specific customer, match customer id and return all their orders
@app.get("/customers/{customer_id}/orders")
def list_orders(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()
