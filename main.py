import json

def afficher_taches(taches):
    print("Liste des tâches :")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache['nom']} {'(Complet)' if tache['complet'] else ''}")

def ajouter_tache(taches, nouvelle_tache):
    tache = {"nom": nouvelle_tache, "complet": False}
    taches.append(tache)
    print(f"Tâche ajoutée : {nouvelle_tache}")

def supprimer_tache(taches, numero_tache):
    if numero_tache >= 1 and numero_tache <= len(taches):
        tache_supprimee = taches.pop(numero_tache - 1)
        print(f"Tâche supprimée : {tache_supprimee['nom']}")
    else:
        print("Numéro de tâche invalide")

def charger_taches_depuis_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

def sauvegarder_taches_dans_fichier(taches, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        json.dump(taches, fichier)

nom_fichier = "taches.json"

taches = charger_taches_depuis_fichier(nom_fichier)

while True:
    print("\nOptions :")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        afficher_taches(taches)
    elif choix == "2":
        nouvelle_tache = input("Entrez la nouvelle tâche : ")
        ajouter_tache(taches, nouvelle_tache)
        sauvegarder_taches_dans_fichier(taches, nom_fichier)
    elif choix == "3":
        numero_tache = int(input("Entrez le numéro de la tâche à supprimer : "))
        supprimer_tache(taches, numero_tache)
        sauvegarder_taches_dans_fichier(taches, nom_fichier)
    elif choix == "4":
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")

