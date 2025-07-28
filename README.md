# Online Movie Rental Store API

This is a RESTful API built with Flask, SQLAlchemy, and SQLite for a fictional online movie rental store. It serves as a portfolio project to demonstrate backend development, database design, and structured data ingestion from CSV files.

## Project Structure
```text
movie\_rental\_api/
│
├── app.py                   # Main Flask app with API endpoints
├── models.py                # SQLAlchemy ORM models
├── database\_setup.py        # Script to initialize and populate the database
├── movie\_rental.db          # SQLite database file (auto-generated)
├── /data/movie\_app\_datasets/
│   ├── users.csv
│   ├── admin\_users.csv
│   ├── movies.csv
│   ├── rentals.csv
│   ├── payments.csv
│   └── reviews.csv
└── /venv/                   # Python virtual environment
```

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
````

### 2. Install required dependencies

```bash
pip install Flask pandas flask_sqlalchemy
```

### 3. Initialize the database and load sample data

This script drops all existing tables, recreates them, and imports CSV data into the database.

```bash
python3 database_setup.py
```

Note: The CSV files are located in `data/movie_app_datasets/`. Foreign key columns that contain empty values are handled using nullable constraints.

## Running the API

To start the Flask server:

```bash
python3 app.py
```

Once the server is running, navigate to:

```
http://127.0.0.1:5000/users
```

This will return a JSON array of all user records.

## API Endpoints (Read-Only)

| Endpoint       | Description              |
| -------------- | ------------------------ |
| `/users`       | Returns all user records |
| `/admin_users` | Returns all admin users  |
| `/movies`      | Returns all movies       |
| `/rentals`     | Returns all rentals      |
| `/payments`    | Returns all payments     |
| `/reviews`     | Returns all reviews      |

All endpoints return JSON responses.

## Technologies Used

* Flask (Web framework)
* SQLAlchemy (ORM)
* SQLite (Database)
* Pandas (CSV processing)

## Known Limitations

* API is currently read-only
* No authentication or authorization implemented
* Data is assumed to be mostly clean and well-formatted
* Foreign key constraints are nullable for demo purposes

## Planned Enhancements

* Add POST, PUT, DELETE endpoints for full CRUD functionality
* Add query parameters for filtering and searching
* Add pagination for large result sets
* Create automated test suite and Swagger documentation