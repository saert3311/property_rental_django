# Rental django para Talento Digital

Proyecto basado en hitos para M6 y M7 del bootcamp de talento digital,usando django `5.0.6`.

## Iniciar proyecto

Usaremos un entorno virtual usando [virtualenv](https://virtualenv.pypa.io) y [pip](https://pip.pypa.io).

```bash
$ python -m venv onlyflans
$ source onlyflans/bin/activate #sistemas UNIX
$ .\venv\Scripts\activate #sistemas Windows
$ pip install -r requirements.txt
$ cd rental_django
#genera el .env con los datos para la conexion de la base de datos
$ python set_db.py
#importamos los modelos iniciales de regiones y comunas
$ python manage.py loaddata regiones
$ python manage.py loaddata provincias
$ python manage.py loaddata comunas
# Ejecutamos el proyecto.
$ python manage.py runserver

```


## Avances 

* Creacion de proyecto y configuracion de ambiente de desarrollo, con Modelos Inciales, de comunas y regiones (Hito 1)

```bash
#Corremos los tests iniciales para comprobar el estado de los modelos
$ python manage.py test

```