pip install -r requerimientos.txt
cd cea_ddi
python manage.py makemigrations ddi
python manage.py migrate
manage.py loaddata datos_iniciales.json
manage.py createsuperuser