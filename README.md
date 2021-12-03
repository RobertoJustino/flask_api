# flask_api

## Dockerfile 

FROM permet de définir l'image source ;

RUN permet d’exécuter des commandes dans votre conteneur ;

ADD permet d'ajouter des fichiers dans votre conteneur ;

WORKDIR permet de définir votre répertoire de travail ;

EXPOSE permet de définir les ports d'écoute par défaut ;

VOLUME permet de définir les volumes utilisables ;

CMD permet de définir la commande par défaut lors de l’exécution de vos conteneurs Docker.

Une image peut instancier plusieurs conteneurs 

Liste des commandes Docker

Construire une image docker (sert aussi à mettre une nouvelle version de l'app)
docker build -t flask_api .

Lance l'app:
docker run flask_api

Erreur quand un port est déjà alloué, remplacer l'ancien container :

Récupère l'id d'un container : 
docker ps

Stop un container :
docker stop <the_container_id>

Supprime un container :
docker rm <the-container-id>

Fais les 2 du dessus directement.
docker rm -f <the-container-id>

