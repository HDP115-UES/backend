# Setup
Para activar el virtualenvironment, run:   
 ```env/Scripts/Activate```   
 
 Instalación de dependencias:   
 ```
 pip install -r requirements.txt
 ```
Configuración de la base de datos: 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_la_base',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Manejo de las migraciones:

```
python manage.py makemigrations
python manage.py migrate
```

Levantar el servidor:
```
py manage.py runserver
```
