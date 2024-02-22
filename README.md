# Inventory Management API

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate` then `python manage.py make migrations`
6. Run the development server: `python manage.py runserver`

## API Endpoints

- Categories: `/categories/`
  http://127.0.0.1:8000/categories/ - for GET and POST HTTP requests
  http://127.0.0.1:8000/categories/<pk>/ - for PUT, PATCH, DELETE, GET HTTP requests
  
- Products: `/products/`
  http://127.0.0.1:8000/products/ - for GET and POST HTTP requests
  http://127.0.0.1:8000/products/<pk>/ - for PUT, PATCH, DELETE, GET HTTP requests
  
- Orders: `/orders/`
  http://127.0.0.1:8000/orders/ - for GET and POST HTTP requests
  http://127.0.0.1:8000/orders/<pk>/ - for PUT, PATCH, DELETE, GET HTTP requests

## API Documentation

Swagger documentation is available at `/swagger/`
- http://127.0.0.1:8000/swagger/
