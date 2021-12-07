# flask_api

## Dockerfile 

FROM permet de définir l'image source ;

RUN permet d’exécuter des commandes dans votre conteneur ;

ADD permet d'ajouter des fichiers dans votre conteneur ;

WORKDIR permet de définir votre répertoire de travail ;

EXPOSE permet de définir les ports d'écoute par défaut ;

VOLUME permet de définir les volumes utilisables ;

CMD permet de définir la commande par défaut lors de l’exécution de vos conteneurs Docker.


## Liste des commandes Docker

Construire une image docker (sert aussi à mettre une nouvelle version de l'app)
 - docker build . -t flask_api:01

Voir les images:
 - docker images

Lance l'app:
- docker run -p cont:machineLocal -it flask_api

Erreur quand un port est déjà alloué, remplacer l'ancien container :

Affcihe les processus / les containers : 
- docker ps -a (si le container n'est pas run, les processus cachés)

Stop un container :
- docker stop <the_container_id>

Supprime un container :
 - docker rm <the-container-id>

Fais les 2 du dessus directement.
 - docker rm -f <the-container-id>
  
Sert à lancer une commande dans un container déjà lancer
 - docker exec -it <container id> <command> 

Monter un volume.
 
- docker volume create app
 
Sert à run l'application sans la rebuild.
Le docker container va chercher en local notre application directement.
 
- docker run -p 3000:3000 -v /app/ -v$(pwd):/app <image_id>
- docker run -d -v /app/ -v $(pwd):/app flask_api 
