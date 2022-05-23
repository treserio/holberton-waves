# Custom Frontend From Scratch
## Project Info
    You and your team have been contacted by a local, elusive, client. They have a new product and
    they need a responsive website built for them in order to market it online; they know you’ve
    got just the right skill set to craft their vision. Secretive as they are, they have decided
    to NOT give you details about their company, nor give you details on the product they are
    selling. Instead, they hand over to you a simple sentence, which they want you to interpret,
    in order to build the best possible responsive website for them to use as a marketing tool.
    The sentence they give you is:

    “Waves”
## Our Idea !
    WAVES an online guided meditaion community. A place were member can find referances to youtube
    videos that help meditation, mindfulness, and relaxation. You can find inspiration from our
    experienced group leader that have trained for years in Yoga and meditation techniques.

## Objectives
You and your team are tasked with the following:

- Build a 1-3 page website for the product you believe they are selling based on their prompt
- Your website must be locally hosted
- Your website must integrate at least 3 of the following components (some of these you’ve seen before - others you may need to research more)
    - CSS Framework(s) (e.g. Bootstrap, Semantic UI, etc.)
    - JavaScript framework(s)
    - Utilizing a third-party API
    - A backend with a storage system
    - CSS Preprocessor
    - Accessibility
    - Cookies
    - Forms
## Frameworks Used
- [Django](http://djangoproject.com)
- [MySQL](https://www.mysql.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [JavaScript](https://www.javascript.com/)

### Frontend
The site consists of 3 pages:
- [Homepage](https://github.com/treserio/holberton-waves/blob/master/homepage.html)
- [Pricing](https://github.com/treserio/holberton-waves/blob/master/homepage.html)
- [Courses](https://github.com/treserio/holberton-waves/blob/master/courses.html)

### Backend
- [api](https://github.com/treserio/holberton-waves/tree/master/api)
- [django](https://github.com/treserio/holberton-waves/tree/master/django_files)
- [manage](https://github.com/treserio/holberton-waves/blob/master/manage.py)

## Installation
    sudo apt install python3.8-venv
    . .venv/bin/activate
    pip install mysqlclient <-- wheel fail is okay if "Successfully installed ..."
    pip install django
    pip install requests
    pip install djangorestframework
    pip install django-filter
    pip install django-extensions
    pip install django-cors-headers
    django-admin startproject django_files .
    python manage.py runserver

    Migrations for api app:
    python manage.py makemigrations api
    python manage.py migrate api

    To populate db:
    python manage.py runscript initialize_videos

    SQL
    sudo /etc/init.d/mysql start
    CREATE DATABASE IF NOT EXISTS holb_waves;
    CREATE USER 'django-waves'@'localhost' IDENTIFIED BY 'H0Lb-6o7_m38@1l5';
    GRANT ALL PRIVILEGES ON holb_waves.* TO 'django-waves'@'localhost';
    FLUSH PRIVILEGES;

## Bugs

CORS issue when loading our api with django "CORS header 'Access-Control-Allow-Origin' missing"
- able to bypass by turning off CORS locally

#### Contributors
- [Tres](https://github.com/treserio)
- [Tofer](https://github.com/Esoteric918)
- [Ron](https://github.com/ronroeandassociates)
