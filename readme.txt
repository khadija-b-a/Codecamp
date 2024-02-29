Ce fichier README explique les fonctionnalités de notre programme Python conçu pour gérer une liste de tâches. Le programme utilise le module argparse pour permettre à l'utilisateur d'ajouter, modifier, supprimer et afficher des tâches dans un fichier de tâches spécifié.

*** Fonctionnalités *** :

Le programme offre les fonctionnalités suivantes :

1- Ajout de tâches
Pour ajouter une tâche, utilisez la commande "add" Vous devez fournir une description de la tâche et son contexte. Le contexte doit figurer dans le fichier de configration des contexte task_context.txt Par exemple :

python script.py lestaches.txt add "Faire les courses" "Maison"

--> cela ajoutera la tâche "Faire les courses" à la liste de tâches et lui associe le contexte "Maison".

Il est aussi possible d'ajouter une tâche parmis les modèles figurant sur le fichier task_template.txt. Pour cela, il suffit d'utiliser la commande "add_model_task" en précisant l'identifiant du modèle. Par exemple:

python script.py lestaches.txt add_model_task 0

--> cela ajoutera la première tâche de la liste des modèles disponibles. si l'identifiant est invalide, un message d'erreur s'affichera.

2- Modification des tâches et de leurs contextes
Pour modifier une tâche existante, on peut soit :

- modifier sa description en utilisant la commande "modify". Vous devez spécifier l'identifiant de la tâche que vous souhaitez modifier ainsi que la nouvelle description. Par exemple : 

python script.py lestaches.txt modify 2 "Réviser pour l'examen"

--> cela modifiera la tâche d'identifiant 2 pour avoir la nouvelle description "Réviser pour l'examen" en gardant le meme contexte.

- modifier le contexte de la tache en gardant la meme description en utilisant la commande "modicont". Vous devez spécifier l'identifiant de la tâche que vous souhaitez modifier ainsi que le nouveau contexte. Par exemple : 

python script.py lestaches.txt modicont 2 "Ecole"
--> si le contexte en paramètre ne figure pas dans la liste des contextes, l'utilisateur est invité à choisir un contexte parmis ceux de la liste qui s'affiche qui a été récupérée à partir du fichier de configuration task_context.txt .

Les commandes de modification sont aussi applicables sur les modèles de tâches qui ont été ajoutés soit après leur ajout à travers les commandes "modify" et "modicont" soit au moment de l'instanciation. Il est possible de choisir un modele de taches et modifier soit son contexte soit sa description avant l'ajout: 

      - pour modifier le contexte du modèle au moment de l'instanciation, on ajoute à la commande "add_model_task" la commande "context_model" suivie du paramètre contexte. Par exemple:
      
      python script.py lestaches.txt add_model_task 0 context_model Education
      
      --> cela ajoutera la première tâche de la liste des modèles disponibles en mettant Education comme contexte
      
      - pour modifier la description du modèle au moment de l'instanciation, on ajoute à la commande "add_model_task" la commande "description_model" suivie du paramètre description. Par exemple:
      
      python script.py lestaches.txt add_model_task 0 description_model "Aller en cours"
      
      --> cela ajoutera la première tâche de la liste des modèles disponibles en mettant la nouvelle description 

3- Suppression de tâches

Pour supprimer une tâche, utilisez la commande rm. Vous devez spécifier l'identifiant de la tâche que vous souhaitez supprimer. Par exemple :

python script.py lestaches.txt rm 3

--> cela supprimera la tâche ayant l'identifiant 3 de la liste de tâches.

4- Affichage de la liste de tâches
Pour afficher la liste de toutes les tâches, utilisez la commande show. Par exemple :

python script.py lestaches.txt show

--> cela affichera toutes les tâches dans le fichier de tâches sous le format d'un tableau de 3 colonnes: identifiant, description et contexte. si le fichier lestaches.txt est vide (il n'y a aucune tache), un message d'erreur s'affichera.

*** Utilisation ***:
Pour utiliser le programme, exécutez le script Python en spécifiant le nom du fichier de tâches et la commande souhaitée. Par exemple :

python script.py lestaches.txt add "Acheter du lait" "Courses"

Assurez-vous que le fichier de tâches spécifié existe avant d'exécuter le programme.

*** Remarques *** :
- Les tâches sont stockées dans un fichier texte spécifié par l'utilisateur (dans cet exemple, "lestaches.txt").
- Chaque tâche a un identifiant unique associé à elle.
- Le programme gère les erreurs telles que la tentative de modification ou de suppression d'une tâche inexistante.
- Le format d'une tâche étant le suivant: {id} {description} {contexte}, on considère qu'un contexte est composé d'un seul mot.
- N'hésitez pas à utiliser ce programme pour gérer vos listes de tâches personnelles. Vous pouvez facilement personnaliser le fichier de tâches et l'adapter à vos besoins.