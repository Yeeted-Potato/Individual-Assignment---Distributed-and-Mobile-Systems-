from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"You asked for customer": customer_id}
