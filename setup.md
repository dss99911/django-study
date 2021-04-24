### 1. Create Virtual environment
    - you can create venv when selecting SDK on Intellij 

### 2. [Create Intellij Project for Django](https://www.jetbrains.com/help/idea/creating-django-project.html)

#### Check django installed. and check version
- check if Terminal is running on virtual environment(shell shows `(venv)`)
```shell
python -m django --version
```

### 3. [Install Django](https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release)
```shell
python -m pip install Django
```

### 4. create Django Project

```shell
django-admin startproject config .
django-admin startproject second_app
```

### 5. setting Django project path on intellij project setting
>Project Settings -> Modules -> <project-name> -> Django

Set project path, and setting path.

Then, you can run django command by tool window
> Tools -> Run manage.py task..

### 6. run server
```shell
python app/manage.py runserver
```

### 7. add app

```shell
python manage.py startapp polls
```

### 8. migration
When using some app, need to prepare some table. so, need migration.
```shell
python manage.py migrate
```