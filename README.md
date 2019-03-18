# PET-STORE

### Prerequisites
the development process utilized the postgres database
install pipenv using Homebrew
```
brew install pipenv
```

**set up the database with a user who has the privileges**
```
- psql postgres
- CREATE DATABASE your_database;
- CREATE USER your_user WITH ENCRYPTED PASSWORD 'your_password';
- ALTER ROLE your_user CREATEDB;
- GRANT ALL PRIVILEGES ON DATABASE your_database TO your_user;
```
### Insatallation
clone the repository
```
git clone https://github.com/ipaullly/pet-store.git
``` 
cd into the pet-store directory and run the command to install all requirements from Pipfile.lock
```
pipenv install
```
Activate the virtual environment
```
pipenv shell
```
Run the tests
```
python manage.py test
```
To activate the server
```
python manage.py runserver
```
## API endpoints
```
POST /api/v1/pets
GET /api/v1/pets
GET /api/v1/pets/<int:id>
PUT /api/v1/pets/<int:id>
DELETE /api/v1/pets/<int:id>
```
## Built with

[Django Rest Framework](https://www.django-rest-framework.org/) - Django