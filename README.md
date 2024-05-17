<h1 align="center">Django ToDo List</h1>
<h3 align="center">A class base view restframework with GenericView classes</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="sqlite" width="90" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>
<a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>
<a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>

</p>

### Demo
It's a preview of the project
![todo](https://github.com/Benfoxyy/Django-CBV-DRF-TodoList/assets/146076866/5fd3133a-0794-43d8-b61d-9a3490bb4239)

### General features
- Class Based View
- Django RestFramewok
- Generic View
- User Authentication

### Todolist features
- Add task
- Edit task
- Delete task

### Setup
To get the repository you need to run this command in git terminal
```bash
git clone https://github.com/Benfoxyy/Django-CBV-DRF-TodoList.git
```

### Getting ready
Create an environment for install all dependencies with this command
```bash
python -m venv venv
```

Install all project dependencies with this command
```bash
pip install -r rquirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and ru fallowing command
```bash
python manage.py makemigrations
```

This command will create all migrations file to database

Now, to apply this migrations run following command
```bash
python manage.py migrate
```

### Option
For editing or manage the database, you shulde be superuser and have superuser permission. So lets create superuser
```bash
python manage.py createsuperuser
```
- Email
- Password
- Password confirmation

### Run server
And finally lets start server and see and using the app
```bash
python manage.py runserver
```

Whene server is up and running, go to a browser and type http://127.0.0.1:8000

### Database shema
![drawSQL-image-export-2024-05-17](https://github.com/Benfoxyy/Django-CBV-DRF-TodoList/assets/146076866/f9f4ecbf-db1a-45d0-9aea-ee352256062d)

<hr>

<h3 align='center'>Thanks for visiting my app, if you have any opinions or seeing bugs; let me know 🙂</h3>