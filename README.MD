-Correr "env/Scripts/Activate" o 
-Borrar contenido en apps.py
-Declarar la carpeta completa para importar los models
-Declarar cada uno de los modelos en setting.py en la carpeta raiz
-Configurar la base de datos para que sea accesible para la aplicación
-Para conectar con la base de datos es necesario instalar el syscopg2

'pip install psycopg2-binary'


-Configuración de la base de datos: 
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
#para instalar los requerimientos
pip install -r requirements.txt

#manejo de las migraciones
python manage.py makemigrations

python manage.py migrate