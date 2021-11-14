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



# Consideraciones
- Para hacer la prueba, he usado un proyecto que creé para aprender django hace meses, basándome en un ejemplo de la propia página de django. He intentado añadir en la medida de lo posible todas las buenas práctias que he ido aprendiendo durante mi carrera profesional. El proyecto intenta seguir la arquitectura hexagonal (o puertos y adaptadores), separando por carpetas el domain, application e infrastucture. He intentado desacoplar al máximo cada capa para hacer la aplicación lo más escalable posible. Esta arquitectura es la que estoy aprendiendo y actualmente, tendrá mil fallos y lagunas pero lo he aplicado lo mejor que he sabido.
- Ya que la prueba es para acceder a un puesto de back, he creado un diseño mínimo navegable para centrarme en la api.
- He creado una batería de tests básica para cubrir las funcionalidades más críticas. (No quería demorar más la entrega cubriendo todos los posibles casos de error)

Ha habido casos en los que he tenido que tomar algunas decisiones de negocio para crear la solución:

- Me ha parecido más real que el campo "dead" de un Author sea opcional ya que es una posibilidad 100% real que se daría en una aplicación de gestión de libros
- Existía el problema en el que, debido a que un book debe tener un author y una o varias categories, ¿qué pasa cuando se elimina un author o una category? Pues se podrían dar varios escenarios, entre ellos:
    a) No borrar el book relacionado, si no dejar a null su relación
    b) Borrar el book relacionado 
- Debido a los problemas que he tenido que me han impedido trabajar todo lo que tenía planeado en esta prueba, me he decantado por la opción b, borrar la relación. Era la más sencilla y rápida.
- Si hubiera desarrollado la otra opción, podría haberme decantado por varias soluciones, entre ellas:
    a) En el handler correspondiente (si elimino author, en el delete_author_handler) debería de haber buscado el book asociado y haberlo eliminado mediante el book_repository. En el caso de category habría sido más complicado ya que al poder tener más de una, solo debería de eliminar el book si la category que se está eliminando es la última que tiene ese book asociada.
    b) Eliminar el author/category y lanzar un evento con el id del author/category eliminado para que, desde un suscriber, se pueda recibir dicho evento y eliminar el book correspondiente.

>Trabajo futuro:
    - Gestión de usuarios, registro, login, etc.
    - Gestión de excepciones, errores http, etc.
    - Más tests para cubrir la edición de book, author, category así como más posibles casos de error.