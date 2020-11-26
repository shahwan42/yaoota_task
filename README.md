# Yaoota Task

Egyptian National ID checker

## Install (assuming you're using Ubuntu)

- clone the repo `$ git clone git@github.com:shahwan42/yaoota_task.git`
- `cd` into the project directory
- copy `.env.example` to `.env` & update your values

### Using Poetry

- make sure you have `python 3.8.6` installed on your system or in `pyenv` versions
- `$ pip install poetry` to install [poetry](https://python-poetry.org/)
- `$ poetry install` to create a virtualenv and install dependencies

### Using Pip

- create & activate a virtualenv
- install dependencies `$ pip install -r requirements.txt`

## Run & Test

- make sure you're inside the desired venv
- `$ docker-compose up` to run the db server
- `$ ./manage.py test` to run tests
- `./manage.py runserver 8001` run server
- then `POST` [http://localhost:8001/api/nid/check/](http://localhost:8001/api/nid/check/) with payload: `{"id_number": "28311301121341"}` for example, using REST Client like Postman

## Or you can call the endpoint from within VS Code

- open the project in `vs code`
- install the [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
- open the file `api.http`
- You'll see CTA link `Send Request` click on it and you'll get the result
