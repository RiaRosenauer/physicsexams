# physicsexams
This django project is a suggestion for a website helping TUM physics students to organize their learning for exams. 

Currently there are two important branches: 
- main:  a working version of the Website where students can log themselves in, in order to remember the tasks that they already worked on.
- anonymous: a working version of the Website without any user data storage so that no problems with data protection occure.

## installation
Depending on branch:
- main:
    No matter what you do it is very important to create a user calles placeholderuser and a student
    with the placeholderuser as user. If you don't do this, the app will not be running. The following is one suggestion, that certainly works:
    ```console
    foo@bar:~$ pip install -r requirements.txt
    foo@bar:~$ python manage.py makemigrations physicsexamsApp
    foo@bar:~$ python manage.py makemigrations
    foo@bar:~$ python manage.py migrate
    foo@bar:~$ python manage.py createsuperuser
    ```
    Create a superuser for yourself. You can leave the e-mail field empty by simply pressing enter. 
    Remember your password because you need it for the next step:
    ```console
    foo@bar:~$ python manage.py runserver
    ```
    Now copy the url and manually navigate in the url bar to localhost/admin.
    Logyourself in with the created superuser and create a User with the username placeholder.
    Go to the Students model and also create a student there with the placeholder user as user.
    Now **log yourself out** again. The website should be running!
- anonymous:
    ```console
    foo@bar:~$ pip install -r requirements.txt
    foo@bar:~$ python manage.py makemigrations physicsexamsApp
    foo@bar:~$ python manage.py makemigrations
    foo@bar:~$ python manage.py migrate
    ```


## database
In order to use a PostgreSQL database, change the current settings for the database to:
```
DATABASES = {
 
    'default': {
 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
 
        'NAME': 'test',
 
        'USER': 'postgres',
 
        'PASSWORD': 'blablabla',
 
        'HOST': 'localhost',
 
        'PORT': '5432',
 
    }
 
}
```
