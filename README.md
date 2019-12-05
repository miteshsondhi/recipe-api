# recipe-api
Django recipe API

### Run tests
```
docker-compose run app sh -c "python manage.py test && flake8"
```

### Run Server
```
docker-compose run app sh -c "python manage.py runserver && flake8"
```