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
- Create Customer
- Create, Read, Update, Delete Books.
- Create Orders.
- Orders to be accepted must match stock quantities with selected books.
- Accepted Orders Changes Stock Quantities for selected books.

#### Extra Actions
- Filters for orders, books, etc.
- Authentication.
- Customers can only operate on self orders.

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
