## kyduu
---

## Comandos Para ejecutar dentro del contenedor de django, el contenedor tiene que estar levantado, si no lo está podemos ejecutar los comandos en lugar de con "exec" con "run"
###Para crear el proyecto (solo si no está creado).
Dentro de la carpeta django/code ejecutar:
```docker-compose exec web django-admin startproject kyduu .```

Crear APP (si no está creada):
Dentro de la carpeta django/code ejecutar:
```docker-compose exec web django-admin startapp <nombre_app> ```

Instalar una package en django
```docker-compose exec web pip install <python-package>```

Realizar migraciones en la bbdd
```docker-compose exec web python manage.py makemigrations```
```docker-compose exec web python manage.py migrate```

Crear Superusuario en backend kyduu
```docker-compose exec web python manage.py createsuperuser```

###Si se añade un modulo python
Para añadirlo a requirements.txt y poder instalarlo al arrancar el contenedor
```docker-compose exec web pip freeze > requirements.txt```

###Test
Comando para ejecutar todos los test
```docker-compose exec web python manage.py test```

## Acceso a Adminier para ver la BBDD.
http://localhost:8080/
servidor: db
usuario: root
Password: <mirar_env_docker-compose>