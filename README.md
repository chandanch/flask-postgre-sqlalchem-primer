# Flask PostGRES Sqlalchemy Primer

Covers basic concepts of utilizing SQLalchemy ORM with PostGRES DB in an flask app.

## Flask Migrate Commands

1. Intialize a new migration repository: `flask db init`

This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.

2. Generate Migration Scripts:
   `flask db migrate`

This command creates a _migrations_ folder which contains migration scripts

3. Apply Changes to Database: `flask db upgrade`

**Note:** Each time the database models change run the `migrate` and `upgrade` command

## Setup Application

1. Install dependencies: `pipenv install`
2. Activate venv: `pipenv shell`
3. Run Application: `python app.py`
