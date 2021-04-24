# Database

## Reference
- [tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#database-setup)
- [ ] [Avoid race conditions](https://docs.djangoproject.com/en/3.1/ref/models/expressions/#avoiding-race-conditions-using-f)
    - ex) If two users of your website try to vote at exactly the same time, this might go wrong: The same value, let’s say 42, will be retrieved for votes. Then, for both users the new value of 43 is computed and saved, but 44 would be the expected value.
    

## Database Engine
settings.py -> DATABASES

## Create Table
### Define Table
[models](../app/second_app/models.py)

### Add Application on Settings
```python
INSTALLED_APPS = [
    'second_app.apps.SecondAppConfig'
]
```

### make migration file
```shell
python manage.py makemigrations second_app
```

0001 version migration file created(django recognize the version. and if there is new version. then migrate.)
```log
Migrations for 'second_app':
  second_app/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

### Check migration SQL
```shell
python manage.py sqlmigrate second_app 0001
```

### reflect migration
```shell
python manage.py migrate
```
migration data is managed on `django_migrations` table on datababase
```log
Running migrations:
  Applying second_app.0001_initial... OK
```

## Use Database
refer to [usage](../app/second_app/models.py)