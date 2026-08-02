# Customer Orders API

A small web application for COMP713 Individual Assignment. A client communicates with my FastApi server, which uses SQLite database to store data. Customers and their orders get managed with a order status workflow.

# Software/Tools Required
- Python
- pip

# To Setup
1. Clone this repository
2. Open terminal in the project folder
3. Create a virtual enviroment

e.g Windows Powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

4. Install the dependancies

pip install -r requirements.txt

# Starting the server

uvicorn main:app --reload

Browser:
http://127.0.0.1:8000 - client interface
http://127.0.0.1:8000/docs - API documentation

# API endpoints

GET - '/heath' - Health check (returns status)
GET - '/customers' - List all customers
POST - '/customers' - Create a customer
GET - '/customers/{id}' - Get one customer
POST - '/customers/{id}/orders' - Create an order for a customer
GET - 'customers/{id}/orders' - List a customers orders
PATCH - '/orders/{id}' - Update an order's status

# Order status workflow

Orders transit through these statuses
pending -> paid -> shipped -> delivered

# Testing the main functions

The system can be tested through the client page or the `/docs` interface:

Create a customer — via the form or `POST /customers`.
Create an order — provide an existing customer ID.Invalid input — submitting a customer without a name returns a 422 error.
Missing customer — requesting `/customers/999` returns a 404 error.
Illegal status change — patching an order from `pending` to `delivered` returns a 400 error.

# Known limitations

- No authentication
- SQLite is not intended for high-concurrency use
