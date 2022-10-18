# KARTOZA TEST JOB

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/anandpandayyy/kartoza_test_job.git
$ cd kartoza_test_job
```

Create a virtual environment to install dependencies in and activate it:

Ubuntu
```sh
$ sudo apt install python3-venv
$ python3 -m venv env
$ source env/bin/activate
```

Windows
```sh
$ python3 -m venv env
$ env\Scripts\activate
```
or

if python3 is not working try that code
```sh
$ python -m venv env
$ env\Scripts\activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py migrate
```

Then we have to create some dummy user that will show in map. So their is a managment command that will add 5 user in database.
```sh
(env)$ python manage.py create_users
(env)$ python manage.py runserver
```
And navigate to [click here to LOGIN](http://127.0.0.1:8000/login/)

In order to test all user you have to login from the superuser account so their is credential of a super user

`username`:`john`

`password`:`admin@123`

After login you will redirect to the admin home page where only superuser can access all user detail and get cordinate of all users in map and clicking on that icon in map it will pop up detail of user.

## Login/Logout entry

Super user can also check the login , logout activity of all user [click here to check log activity](http://127.0.0.1:8000/admin/admin/logentry/)


## Normal user login

When a normal user login via [click here to LOGIN](http://127.0.0.1:8000/login/)

`username`:`smith`

`password`:`admin@123`

it will redirect to admin login page where he can edit their profile and review it.

## To register new user

[click here to REGISTER](http://127.0.0.1:8000/register/)

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```


