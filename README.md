1. Install postgres
2. Create .env
```
POSTGRES_DBNAME=""
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"

BACKEND_ADDR = 'http://127.0.0.1:8000/api'
DEFAULT_SERVER = 'http://127.0.0.1:8000'
```
3. Create virtual environment
```
python -m venv venv
```
4. Install requirements
```
source venv/bin/activate
pip install -r requirements.txt
```
5. Create database
```
python manage.py create_database
```
6. Do migrations
```
python manage.py migrate
```
7. Create user
```
python manage.py createsuperuser
```
8. Run test server!
```
python manage.py runserver
```