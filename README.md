# IT-Reference-Book

Application Setup
-----------

#### Prerequisites
---
* Python v2.7.6 (programming language)
* Pip v9.0.1 (package manager for python)
* Virtualenv (virtual environments for python projects)

#### Forking & Cloning
---
* First make a fork of this repository to your GitHub account by clicking on the fork button.
* cd into your working directory and **clone your repository**. Replace <your_github_user_id> appropriately.
  ```
  git clone https://github.com/<your_github_user_id>/IT-Reference-Book.git
  ```

#### Project setup
---
* cd into your working directory
  ```
  virtualenv env
  source env/bin/activate
  cd ./referenceBook/
  pip install -r requirements.txt
  ```
* Migrate all your model changes to the database.
  ```
  python manage.py migrate
  ```
* Collect static files
  ```
  python manage.py collectstatic --noinput
  ```
* Next, you need to create a superuser to login to the application.
  ```
  python manage.py createsuperuser
  ```
  * When prompted, enter the following details.
  ```
  Username (leave blank to use 'vagrant'): admin
  Email address: admin@admin.com
  Password:Qwerty1!
  Password (again):Qwerty1!
  ```
* Start the development server.
  ```
  python manage.py runserver 0.0.0.0:8000
  ```
