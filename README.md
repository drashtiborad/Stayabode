TODO Lists Projects

It uses MySQL as Database, so it needs to be installed and enter mysql user credentials in settings.py file.

Also install mysql connector using below command

sudo apt install -y libmysqlclient-dev

To install all dependencies for the projects, run below command:

pip install -r requirements.txt

Before starting the server you need to run the below commands to get your Database setup

python manage.py makemigrations

python manage.py migrate

Both these commands need to be run from the project directory

To create a superuser run the below command and give the credentials as prompted

python manage.py createsuperuser

Once, the above setup is done, you can start get your app running by below command

python manage.py runserver

Below is the list of endpoints (localhost:8000) for various purposes:

/todo/ : Home page which displays a list of all the todo tasks

/create/ : To create a new task

/update/<task_id> : To update existing task

/delete/<task_id> : To delete the task

/task/<task_id> : To get details of specific task id

/admin/todo/todolist/ : For admin operations (Needs login of admin user)

Admin has the below functionalites

> Can export to do list in bulk in CSV format

> Can view all the to do task's, even the ones that are deleted by non-admin users

> List, search and filter based on the various fields



