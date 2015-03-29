#!/bin/sh
# Arriba ejecutamos con sh en entornos unix
# Para los que conocen poco o nada de GIT
# stash es un entorno donde se guardan temporalmente los cambios
#   estos no son guardados en el repositorio ni están "visibles" al usuario
#   son los cambios que se hicieron pero no se necesitan en el commit
# staged es un entorno donde están los archivos que van a ser agregados
#    cuando se ejecute el comando commit
# working es lo que podemos ver esto no será agregado al repositorio

# Tenemos que probar lo que esta en staged funciona, lo que se va a subir,
# entonces todos los cambios hechos en working lo
# pasamos a stash y de esta manera tenemos el código
# limpio y sería el mismo de staged
git stash -q --keep-index
# Necesitamos que cumpla con el PEP8 para asegurar cierta calidad.
# Ignoramos E501 que habla de la longitud de linea
# ya poseemos pantallas que manejan mayor cantidad
# de caracteres así que no es necesario Django también las ignora.
pep8 --show-source --statistics --ignore=E501,E402 .
PEP8_RESULT=$?
# Corremos los tests y vemos si cumple el el mínimo requerido
python manage.py test
RESULT=$?
# Ahora restauramos los cambios para que el usuario no pierda
# lo último que edito y no estaba listo para el commit.
git stash pop -q

if [ $PEP8_RESULT -ne 0 ]
   then
       echo ""
	   echo "Project is not following PEP8!!!" >&2
fi
# Si no cumple PEP8 o el coverage no hace el commit.
[ $RESULT -ne 0 ] || [ $PEP8_RESULT -ne 0 ] && exit 1
exit 0
