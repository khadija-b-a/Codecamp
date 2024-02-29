import argparse
from io import StringIO


def add_task(description, contexte, filename):
  task_contexts = load_task_contexts('task_context.txt')
  # vérifier si le contexte existe dans le fichier de configuration
  while contexte not in task_contexts:
    print(contexte)
    print("Voici les contextes possibles")
    print(task_contexts)
    contexte = input("Entrez le nouveau contexte \n")
  # lecture du fichier en mode ajout
  with open(filename, 'r+') as lestaches:
    lines = lestaches.readlines()
    # recherche du dernier identifiant
    last_id = 1 if not lines else int(lines[-1].split()[0]) + 1
    # ajout de la tâche avec l'identifiant associé
    if not isinstance(description, StringIO):
      description = " ".join(description)
    lestaches.write(f"{last_id} {description} {contexte} \n")
    # retourner l'identifiant
    print("TaskID : " + str(last_id))
    return (last_id)


def modify_task(new_description, id, filename):
  # déclaration d'une booléenne déterminant si l'identifiant existe ou pas
  search = False
  with open(filename, 'r') as lestaches:
    lines = lestaches.readlines()
  with open(filename, 'w') as lestaches:
    # recherche de l'identifiant dont on souhaite modifier la description de tache
    for line in lines:
      current_id, current_context = int(line.split()[0]), line.split()[-1]
      if current_id == id:
        search = True
        # si l'id est trouvé on écrit la nouvelle description
        joined_string = " ".join(new_description)
        lestaches.write(f"{id} {joined_string} {current_context} \n")
      else:
        lestaches.write(line)
    if search is False:
      print(f"la tache d'identifiant {id} est introuvable")


def modify_context_task(new_context, id, filename):
  # déclaration d'une booléenne déterminant si l'identifiant existe ou pas
  search = False

  # vérifier si le contexte existe dans le fichier de configuration
  task_contexts = load_task_contexts('task_context.txt')
  if not isinstance(new_context, str):
    new_context = " ".join(new_context)
  while new_context not in task_contexts:
    print("Voici les contextes possibles")
    print(task_contexts)
    new_context = input("Entrez le nouveau contexte \n")
  with open(filename, 'r') as lestaches:
    lines = lestaches.readlines()
  with open(filename, 'w') as lestaches:
    # recherche de l'identifiant dont on souhaite le contexte
    for line in lines:
      current_id = int(line.split()[0])
      current_context = str(line.strip().split()[-1])
      current_description = line[len(line.split()[0]) +
                                 1:line.find(current_context)]
      if current_id == id:
        search = True
        # si l'id est trouvé on écrit la nouvelle description
        lestaches.write(f"{id} {current_description} {new_context} \n")
      else:
        lestaches.write(line)
    if search is False:
      print(f"la tache d'identifiant {id} est introuvable")


def delete_task(id, filename):
  # déclaration d'une booléenne déterminant si l'identifiant existe ou pas
  search = False
  with open(filename, 'r') as lestaches:
    lines = lestaches.readlines()
  with open(filename, 'w') as lestaches:
    for line in lines:
      # recherche de l'identifiant de la tâche qu'on souhaite supprimer
      current_id = int(line.split()[0])
      # si l'id est trouvé on ne fait rien
      if current_id == id:
        search = True
      # sinon on reécrit la ligne
      else:
        lestaches.write(line)
    if search is False:
      print(f"la tache d'identifiant {id} est introuvable")


def show_tasks(filename):
  COLOUR = "\033[92m"  #GREEN
  RED = "\033[91m"
  BOLD = "\033[1m"
  RESET = "\033[0m"
  with open(filename, 'r') as lestaches:
    lines = lestaches.readlines()
    if (len(lines) != 0):

      #max id length
      id_len = max(2, max(len(line[0:len(line.split()[0])]) for line in lines))
      #max context lenfth
      context_len = max(8, max(len(line.split()[-1]) for line in lines))
      # tri des lignes par ordre croissant des identifiants
      lines.sort(key=lambda x: int(x.split()[0]))
      # On print la cartouche
      taille = max(12,
                   max(len(line) - id_len - context_len -2 for line in lines))
      print('+' + id_len * '-' + '+' + taille * '-' + '+' + context_len * '-' +
            '+')
      print('|' + f"{COLOUR}ID" + (id_len - 2) * ' ' + f"{RESET}|" + f"{COLOUR}Description" +
            (taille - 11) *' ' + f"{RESET}|" + f"{COLOUR}Contexte" +
            (context_len - 8) * ' ' + f"{RESET}|")
      print('+' + id_len * '-' + '+' + taille * '-' + '+' + context_len * '-' +
            '+')
      for line in lines:
        id = str(line.strip().split()[0])
        contexte = str(line.strip().split()[-1])
        descrip = line[len(line.split()[0]) + 1:line.find(contexte)]
        descrip = descrip.strip()
        print('|' + id + (id_len - len(str(id))) * ' ' + '|' + descrip +
              (taille - len(descrip)) * ' ' + '|' + contexte +
              (context_len - len(contexte)) * ' ' + '|')
        print('+' + id_len * '-' + '+' + taille * '-' + '+' +
              context_len * '-' + '+')
    else:
      print(f"{RED}Aucune tache trouvée")


def load_task_contexts(file_path):
  task_contexts = []
  with open(file_path, 'r') as task_contexts_file:
    lines = task_contexts_file.readlines()
    for line in lines:
      context_description = line.strip()
      task_contexts.append(context_description)
  return task_contexts


def load_task_contexts(file_path):
  task_contexts = []
  with open(file_path, 'r') as task_contexts_file:
    lines = task_contexts_file.readlines()
    for line in lines:
      context_description = line.strip()
      task_contexts.append(context_description)
  return task_contexts


def add_model_task_func(n, file_path):
  with open('task_template.txt', 'r') as file:
    task_models = file.readlines()
  if n > len(task_models):
    print(f"La tâche modèle numéro {n} ne figure pas dans les modèles")
  else:
    task = task_models[n].strip()
    context = (task.split()[-1])
    description = task[0:task.find(context)].split()
    id = add_task(description, context, file_path)
    return (id)


def main():
  parser = argparse.ArgumentParser()
  #parser.add_mutually_exclusive_group(required=True)
  parser.add_argument('filename', type=str, help='Nom du fichier des tâches')
  subparsers = parser.add_subparsers(dest='command',
                                     help='Commande à exécuter')

  # Commande "add"
  add_parser = subparsers.add_parser('add', help='Ajouter une tâche')
  # Tâche niveau 1 : contexte de réalisation
  add_parser.add_argument('description',
                          nargs='+',
                          help='Description de la tâche')
  add_parser.add_argument('contexte',
                          help='Ajouter un contexte de réalisation')

  # Commande "modify"
  modify_parser = subparsers.add_parser('modify', help='Modifier une tâche')
  modify_parser.add_argument('id', type=int, help='Identifiant de la tâche')
  modify_parser.add_argument('new_description',
                             nargs='+',
                             help="Nouvelle description de la tâche")
  # Commande "modify context"
  modicont_parser = subparsers.add_parser(
      'modicont', help="Modifier le contexte d'une tâche")
  modicont_parser.add_argument('id', type=int, help='Identifiant de la tâche')
  modicont_parser.add_argument('new_context',
                               nargs='+',
                               help="Nouveau contexte de la tâche")

  # Commande "rm"
  remove_parser = subparsers.add_parser('rm', help='Supprimer une tâche')
  remove_parser.add_argument('task_id',
                             type=int,
                             help='Identifiant de la tâche')

  # Commande "show"
  subparsers.add_parser('show', help='Afficher la liste des tâches')

  # Commande "add model task"
  model_task_parser = subparsers.add_parser(
      'add_model_task', help='Ajoute une task suivant les modèles prédéfinis')
  model_task_parser.add_argument(
      'nb',
      type=int,
      help='numéro de la tâche du panneau de configuration à ajouter')

  model_task_subparsers = model_task_parser.add_subparsers(
      dest='command_model', help='Commande à exécuter')

  # Subparser description des taches modeles
  description_model = model_task_subparsers.add_parser(
      'description_model',
      help='modifie la description d\'une tache model à l\'instanciation')

  description_model.add_argument(
      'text',
      nargs='+',
      type=str,
      help='text de la description a associé à la tache model')

  #subparser contexte des taches modeles
  context_model = model_task_subparsers.add_parser(
      'context_model',
      help='modifie le contexte d\'une tache model a l\'instanciation')
  context_model.add_argument('contex',
                             help='modifie le contexte d\'une tache modele')

  args = parser.parse_args()
  if (args.filename != ''):
    if (args.command == 'add'):
      add_task(args.description, args.contexte, args.filename)
    elif (args.command == 'modify'):
      modify_task(args.new_description, args.id, args.filename)
    elif (args.command == 'rm'):
      delete_task(args.task_id, args.filename)
    elif (args.command == 'show'):
      show_tasks(args.filename)
    elif (args.command == 'modicont'):
      modify_context_task(args.new_context, args.id, args.filename)
    elif (args.command == 'add_model_task'):
      id = add_model_task_func(args.nb, args.filename)
      if (args.command_model == 'description_model'):
        modify_task(args.text, id, args.filename)
      elif (args.command_model == 'context_model'):
        modify_context_task(args.contex, id, args.filename)
    else:
      print("commande introuvable !")
  else:
    print("Veuillez vérifier le nom de fichier !")


if __name__ == "__main__":
  main()
