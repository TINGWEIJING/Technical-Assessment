# MoneyLion Technical Assessment

- [MoneyLion Technical Assessment](#moneylion-technical-assessment)
  - [Setup](#setup)
    - [Requirements](#requirements)
    - [Local (Linux environment)](#local-linux-environment)
      - [Running](#running)
      - [Unit Test](#unit-test)
      - [Unit Test with Coverage](#unit-test-with-coverage)
    - [Using Docker](#using-docker)
      - [Docker](#docker)
      - [Unit Test](#unit-test-1)
      - [Unit Test with Coverage](#unit-test-with-coverage-1)
    - [Override environment variables using `.env`](#override-environment-variables-using-env)
  - [API Endpoints](#api-endpoints)
  - [Available Sample Data in Database](#available-sample-data-in-database)
    - [`user` table](#user-table)
    - [`feature` table](#feature-table)

## Setup
### Requirements
- Python 3.8 or above

### Local (Linux environment)
1. Create Python virtual environment.
    ```bash
    python -m venv venv
    ```

2. Activate the environment.
    ```bash
    source ./venv/bin/activate
    ```

3. Install all the required dependencies.
    ```bash
    pip install -r ./requirements.txt
    ```

#### Running
1. Make sure the environment is activated.
    ```bash
    source ./venv/bin/activate
    ```

2. Initialize the database (sqlite).
    ```bash
    python -m app.init_db ./app/init_db.py
    ```

3. Start the server.
    ```bash
    uvicorn app.main:app --host "127.0.0.1" --port 8000
    ```

4. Interact the API endpoints with base url http://127.0.0.1:8000/.
   Example:
    ```bash
    curl -X 'GET' \
      'http://127.0.0.1:8000/feature?email=thomas%40gmail.com&featureName=Dark%20theme%20UI' \
      -H 'accept: application/json'
    ```

5. Access the interactive API documentation Swagger UI at http://127.0.0.1:8000/docs

6. Access the alternative API documentation ReDoc at http://127.0.0.1:8000/redoc

#### Unit Test
1. Make sure the environment is activated.
    ```bash
    source ./venv/bin/activate
    ```

2. Run the `test.sh` script.
    ```bash
    ./script/test.sh
    ```

#### Unit Test with Coverage
1. Make sure the environment is activated.
    ```bash
    source ./venv/bin/activate
    ```

2. Run the `coverage-test.sh` script.
    ```bash
    ./script/coverage-test.sh
    ```

3. Generate the coverage html report and access it at `./htmlcov/index.html`.
    ```bash
    coverage html
    ```


### Using Docker
1. Build the image.
    ```bash
    docker build -t "ting-technical-assessment-img" .
    ```

#### Docker
1. Start the container.
    ```bash
    docker container run -it \
      --name "ting-technical-assessment" \
      -p 80:80 \
      -v ting-technical-assessment-db:/code/database \
      "ting-technical-assessment-img" ./script/run.sh
    ```

2. Interact the API endpoints with base url http://0.0.0.0/.
   Example:
    ```bash
    curl -X 'GET' \
      'http://0.0.0.0/feature?email=thomas%40gmail.com&featureName=Dark%20theme%20UI' \
      -H 'accept: application/json'
    ```


1. Access the interactive API documentation Swagger UI at http://0.0.0.0/docs

2. Access the alternative API documentation ReDoc at http://0.0.0.0/redoc


#### Unit Test
1. Start the container with script.
    ```bash
    docker container run --rm \
      "ting-technical-assessment-img" ./script/test.sh
    ```

#### Unit Test with Coverage
1. Start the container with script.
    ```bash
    docker container run --rm \
      "ting-technical-assessment-img" ./script/coverage-test.sh
    ```

### Override environment variables using `.env`
1. Copy the `sample.env` file and rename it to `.env`.

2. Modify the values.

3. For running locally, just run the command below. The `.env` file will be read automatically.
    ```bash
    uvicorn app.main:app --host "127.0.0.1" --port 8000
    ```

4. For running using Docker, use the command below:
    ```bash
    docker container run -it \
      --name "ting-technical-assessment" \
      -p 80:80 \
      -v ting-technical-assessment-db:/code/database \
      --env-file ./.env \
      "ting-technical-assessment-img" ./script/run.sh
    ```



## API Endpoints
List of available API endpoints can be view on http://127.0.0.1:8000/redoc (running locally) or http://0.0.0.0/redoc (docker).

For technical assessment requirements:
| Method | URL Pattern                        |
| ------ | ---------------------------------- |
| GET    | /feature?email=XXX&featureName=XXX |
| POST   | /feature                           |

Extra:

| Method | URL Pattern          |
| ------ | -------------------- |
| GET    | /admin/users/        |
| POST   | /admin/users/        |
| GET    | /admin/users/{id}    |
| DELETE | /admin/users/{id}    |
| GET    | /admin/features/     |
| POST   | /admin/features/     |
| GET    | /admin/features/{id} |
| DELETE | /admin/features/{id} |

## Available Sample Data in Database
- **All feature accesses are not enabled by default in the database.**

### `user` table
| id  | email            |
| --- | ---------------- |
| 1   | thomas@gmail.com |
| 2   | leo@gmail.com    |
| 3   | ali@gmail.com    |


### `feature` table
| id  | name            |
| --- | --------------- |
| 1   | Dark theme UI   |
| 2   | Multi-tab       |
| 3   | Export to PDF   |
| 4   | Import from CSV |
