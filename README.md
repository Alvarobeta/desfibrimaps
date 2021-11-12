# Instrucciones para usar el proyecto
> Aquí van las instrucciones para ejecutar el proyecto según se facilita

Suponiendo que tienes Docker y docker-compose instalado, simplemente usa
`docker-compose up` para levantar los servicios.

Deberias tener la aplicación corriendo en `http://localhost:8000`
y la base de datos en `localhost:3306`, con user `root` y password `root` (sí, sé que no es muy seguro esto...)

La primera vez que levantes el servicio, puedes cargar datos y la estructura de la base de datos con `docker-compose run web_service python manage.py migrate`.

Si falta algún paquete que se haya saltado el `docker-compose up`, puedes usar `docker-compose build` para instalar los requirements.

Para ejecutar los test, simplemente lanza `docker-compose run web_service python manage.py test`

Cuando hayas terminado, recuerda que puedes limpiar todos los contenedores y datos con `docker-compose rm -v -s -f` (y recuerda limpiar las imagenes de vez en cuando!)


>ENUNCIADO:
Hola Alvaro,

Soy Manuel de Doofinder. Como ya te comenté en la entrevista el siguiente paso es una prueba técnica. No hay límite de tiempo.

El objetivo del ejercicio es desarrollar una aplicación para gestionar el catálogo de libros de una biblioteca. 
Como usuario, debería poder 

- DONE consultar el catálogo, 
- DONE - dar de alta nuevos libros y 
- DONE - modificar o 
- DONE - eliminar los existentes, 
- (Depending on business decision) y entidades relacionadas, en una o sucesivas sesiones de trabajo.

Un libro deberá tener al menos la siguiente información:
-ISBN
-Título
-Autor
-Descripción
-Categorías

Un Autor deberá tener la siguiente información:
-Nombre completo
-Pseudónimo (opcional)
-Fechas de nacimiento y muerte

Una Categoría deberá tener la siguiente información:
-Nombre
-Descripción (opcional)

No hay ningún requisito en cuanto al stack tecnológico, puedes utilizar el que prefieras. No puedes usar plataformas tipo WordPress, pero sí puedes utilizar frameworks y librerías siempre que pueda distinguirse bien el código propio.

Aunque no es un requisito, para puestos Full Stack Front, valoraremos positivamente:

La utilización de código JavaScript puro (vanilla) así como el uso de estilos CSS propios.

Los detalles de experiencia de uso de la aplicación, como diálogos de confirmación, validaciones…

IMPORTANTE: La aplicación a entregar debe incluir un fichero README con instrucciones suficientes para ponerla en marcha y poder probarla. Es recomendable usar contenedores Docker para desplegar la prueba o, si se desea, se puede utilizar la capa gratuita de algún servicio de hosting tipo Heroku para alojar la aplicación.

Si tienes cualquier duda, problema, o necesitas algo de orientación puedes escribirme cuando quieras.

Un saludo.

