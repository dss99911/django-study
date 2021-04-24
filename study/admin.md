#Admin

## reference
- [tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-an-admin-user)
- [tutorial2 - customizing admin page](https://docs.djangoproject.com/en/3.1/intro/tutorial07/)


## Create admin user
```shell
python manage.py createsuperuser
```

## Manage Database on Admin page
[admin](../app/second_app/admin.py)
```python
from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)
```