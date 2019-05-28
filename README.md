# PET-STORE
[![Build Status](https://travis-ci.org/ipaullly/pet-store.svg?branch=ch-setup-continuous-coverage)](https://travis-ci.org/ipaullly/pet-store) [![Coverage Status](https://coveralls.io/repos/github/ipaullly/pet-store/badge.svg?branch=ch-setup-continuous-coverage)](https://coveralls.io/github/ipaullly/pet-store?branch=ch-setup-continuous-coverage) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/7a80a9487009409896d40951636ff8aa)](https://www.codacy.com/app/ipaullly/pet-store?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ipaullly/pet-store&amp;utm_campaign=Badge_Grade)
### Links
the API was built using Django Rest Framework (DRF) available at:
- [Swagger API documentation](https://pet-store-api.herokuapp.com/api/v1/swagger/)
- [Redoc API documentation](https://pet-store-api.herokuapp.com/api/v1/redoc/)

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
