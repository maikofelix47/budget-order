# Budger Order Project

## Set Up
- Install python 3
- Install django
- Install django-environ `python3 -m pip install django-environ`
- Create .env file with the following configuration
  ```
        SECRET_KEY=secret_key
        DEBUG=True

        DB_ENGINE=db_engine
        DB_NAME=db_name
        DB_USER=username
        DB_PASSWORD=db_password
        DB_HOST=host
        DB_PORT=port

  ```
- Create Migration files `python3 manage.py makemigrations`
- Run Migrations `python3 manage.py migrate`
- Create superuser `python3 manage.py createsuperuser`

## Access
1. Start server `python3 manage.py runserver`
2. Access Admin panel `http://localhost:8000/admin`
3. Access system `http://localhost:8000/`