# Instrucciones para usar el proyecto
> Aquí van las instrucciones para ejecutar el proyecto según se facilita

Suponiendo que tienes Docker y docker-compose instalado, simplemente usa
`docker-compose up` para levantar los servicios.

Deberias tener la aplicación corriendo en `http://localhost:8000`
y la base de datos en `localhost:3306`, con user `root` y password `root` (si, sabemos que no es muy seguro esto...)

La primera vez que levantes el servicio, puedes cargar datos y la estructura de la base de datos con `docker-compose run web_service python manage.py migrate`

Cuando hayas terminado, recuerda que puedes limpiar todos los contenedores y datos con `docker-compose rm -v -s -f` (y recuerda limpiar las imagenes de vez en cuando!)

En el caso que prefieras usar otros frameworks , siempre puedes usar estos pasos para llenar la base de datos!

> Si realizas cambios en la infraestructura, por favor, indicalo aquí

