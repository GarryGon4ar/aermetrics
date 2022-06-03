# Test task



## Build and run



```bash
docker-compose up --build
docker exec -ti aermetrics_web_1 python manage.py migrate
```

## Endpoints

```python
GET /api/types - list of types
GET /api/aircrafts - list of aircrafts
GET /api/statuses - list of statuses

POST /upload - upload csv file with data
    
GET /statistics/<query params> - get data by every type, aircraft or status

e.g .../statistics/?status=Finished
 
```

PS. I haven't prepared environment for productions use(uwsgi or gunicorn instead of runserver, 
volume for db, entrypoint or sth to get rid of manual command to run migrations)

