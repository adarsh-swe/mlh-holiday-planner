# mlh-holiday-planner

## Dev Environment

Make a local copy of `.env` file following `example.env`

To start development environment:

```
$ docker-compose up --build -d
```

Any changes to HTML front-end and back-end will be reflected by hitting refresh in the browser.
To install additional Flask packages, re-run docker-compose up build command.

## Usage

Create a .env file with the following line included:

```bash
URL=localhost:5000
```

Start psql container using `$ docker-compose up -d`

Start flask development server

```bash
$ export FLASK_ENV=development
$ flask run
```

## To use the '/flightsAPI' endpoint:

-   make sure the api key is added in .env
-   call the endpoint with a POST request containing the following data (as key-value/ form data):
    -   origin = origin airport code
    -   destination = destination airport code
    -   departDate = date of departure
    -   returnDate = date of arrival

EXAMPLE:

```bash
origin:YYZ
destination:YVR
departDate:2021-09-01
returnDate:2021-12-01
```

_Note: for testing purposes, just use the exact form data above_
