# django gulp template

## install

### virtualenv
```
$ virtualenv -p `which python3.6` venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


### migration
you should create database 'sample' before migration.

```
$ python manage.py migrate
```

### create super user
```
$ python manage.py createsuperuser
```

### run
```
$ gulp
```

### admin page
```
http://localhost:8000/admin/
```

### create a project
```
$ django-admin startproject config .
```

### create a app
```
$ python manage.py startapp sample
```
