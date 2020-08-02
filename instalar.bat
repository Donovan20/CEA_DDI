pip install -r requerimientos.txt
cd cea_ddi
python manage.py makemigrations ddi
python manage.py migrate
django-admin loaddata datos_iniciales