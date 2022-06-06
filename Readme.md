# Test task



## Build and run



```bash
docker-compose up --build
docker exec -ti aermetrics_web_1 python manage.py migrate
```

## Endpoints

```python
GET api/ - get statistics by every aircraft, status and type

POST api/upload - upload csv file with data
 
```

PS. I haven't prepared environment for productions use(uwsgi or gunicorn instead of runserver, 
volume for db, entrypoint or sth to get rid of manual command to run migrations, retrieved env variables)

