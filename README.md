# Book Store App in Django

## How To Run
### Basic Requirements
- python3.9
- pip 23.0.1
- python3 env
- Postgres PSQL
---

### Repository and Dependencies
- Clone Repository (main branch its the release)
- Create a new env `python -m venv path/to/your/env`
- Activate your new env `source path/to/your/env/bin/activate/`
- Install requirements `pip install -r requirements.txt`


### Database
- `sudo -U postgres psql`
- `create database bookstore;`
- `create user bookstore_user;`
- `alter user bookstore_user with encrypted password 'bookstore_p@ssword';`
- `alter user bookstore_user with superuser;`
- `grant all privileges on database bookstore to bookstore_user;`

### Run Project
- Just for simplicity, provided
- dotenv on `./bookstore/.env`
#### on project root `bookstore/bookstore`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

### Test 
#### on project root `bookstore/bookstore`
- `python manage.py migrate` (only if not migrated before)
- `python manage.py test`

### Endpoints
#### Swagger
- http://127.0.0.1:8000/swagger/
#### Insomnia
- https://insomnia.rest/download
- Exported Endpoints Located at `./bookstore_endpoints.json`

  
---

#### Actions

#### Authentication
- POST `/auth/token/`
    - username, password
    - Generate refresh, and access Tokens
- POST `/auth/token/refresh/`
    - refresh
    - Refresh token
- POST `/auth/token/verify/`
    - token
    - Verify token

#### Customers
- GET `/customers/`
    - IsAuthenticated or IsAdmin
    - List
        - Authenticated User, return only self
        - SuperUser, retruns all created customers
    - Retrieve
       - Return self
- POST `/customers/`
    - AllowAny 
    ```json
      {
          "user": {
              "username": "username",
              "email": "email@email.com"
              "password": "pass_example"
          },
          "name": "name",
          "cpf": "cpf_number",
          "phone": "phone_number"
      }
    ```
#### Books
- BookCategory
    - POST `/books/category/`
        - IsAdmin
        ```json
          {
              "name": "category_name"
          }
        ```
    - GET `/books/category/`
         - IsAuthenticated
         - List and Retrieve
- BookAuthor
    - POST `/books/author/`
        - IsAdmin
        ```json
          {
              "name": "author_name"
          }
        ```
    - GET `/books/author/`
         - IsAuthenticated
         - List and Retrieve
- Book
    - GET `/books/book/`
        - IsAuthenticaated
        - List and Retrieve
        - Filters: title, release_year, auhtor, category
        - order_by: any model field (ex.: created, -created, modified, etc)
    - POST `/books/book/`
        - IsAdminUser
        ```json
          {
            "title": "book_title",
            "release_year": 1929,
            "quantity": 29,
            "author": "uuid4",
            "category": "uuid4",
          }
        ```
    - PATCH `/books/book/`
        - IsAdminUser 
    - PUT `/books/book/`
        - IsAdminUser
    - DELETE `/books/book/`
        - IsAdminUser
#### Checkout
- Order
    - GET `/checkout/orders/`
        - IsAuthenticated: returns orders made by self user
        - IsAdmin: returns all orders
        - Filters: customer_name, customer_cpf, release_year, author, category
        - order_by: any model field (ex.: created, -created, modified, etc)
    - POST `/checkout/orders/`
        - IsAuthenticated
        - Must have a Customer
        ```json
           {
              "book": "uuid4",
              "quantity": 3
           }
        ```   
---               
#### Entities
##### Basic Entities
- Book
- Order
- Customer

##### Extras
- BaseModel
- AuthUser
- BookAuthor 
- BookCategory


##### Relations
![bookstore_buzz](https://github.com/carvalheiracarlos/bookstore/assets/102188162/e5ebb059-5049-4540-be7c-b73e3790c6ba)
