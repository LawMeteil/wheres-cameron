# Groupe de sbai_s 979661

Where's Cameron est une application créée en Python dont le but est de retrouver un visage dans une vidéo et de renvoyer les frames (les images) où le visage importé apparait. L'application utilise un service de Microsoft Azure appelé "Face API" qui va gérer lui-même la reconnaissance faciale entre plusieurs médias. Vous aurez donc besoin d'un compte Azure pour pouvoir lancer le script.

Dans un premier temps, exécutez le `install.sh` qui va lancer l'installation des différentes librairies nécessaires.

`./install.sh`

Cependant vous ne pouvez pas encore lancer l'application puisqu'il faut avoir un compte et un abonnement Microsoft Azure. Si c'est déjà le cas, vous allez devoir créer un groupe de ressource et y ajouter le service "Face API". Cliquez sur "Accéder à la ressource" et dans l'onglet "Gestion des ressources", cliquez sur "Clés et point de terminaison". C'est cette page qui va vous donner un accès à la solution. Copiez la clé 1 et le point de terminaison et collez-les dans le script `api.py` ici :

`API_KEY="PAST YOUR KEY HERE"`
`ENDPOINT="PAST YOUR ENDPOINT HERE"`

Vous êtes maintenant prêt à utiliser l'application !

`python view.py`

Cliquez sur `Browse Image` pour importer une photo de votre PC et ensuite sur `Proceed`. Attendez quelques instants et un dossier avec la date et l'heure de lancement de la solution. Ce dossier sera rempli par des frames de la vidéo avec le visage de la photo importée ! 
