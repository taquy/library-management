
# Installation

```
conda create --name py39 python=3.9

conda activate py39

pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=library.settings

```

# Run application

```
cd backend/library

python manage.py makemigrations

python manage.py migrate 

python manage.py runserver 127.0.0.1:8000
```
