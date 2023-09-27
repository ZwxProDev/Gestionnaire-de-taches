import json
import datetime

def afficher_taches(taches):
    print("Liste des tâches :")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache['nom']} (Échéance : {tache['date_echeance'].strftime('%Y-%m-%d') if 'date_echeance' in tache else 'N/A'}, Catégorie : {tache['categorie'] if 'categorie' in tache else 'Non catégorisé'})")

def ajouter_tache(taches, nouvelle_tache):
    tache = {"nom": nouvelle_tache, "complet": False}
    taches.append(tache)
    print(f"Tâche ajoutée : {nouvelle_tache}")

def ajouter_tache_avec_date(taches, nouvelle_tache, date_echeance):
    tache = {"nom": nouvelle_tache, "complet": False, "date_echeance": date_echeance}
    taches.append(tache)
    print(f"Tâche ajoutée : {nouvelle_tache} (Échéance : {date_echeance.strftime('%Y-%m-%d')})")

def ajouter_tache_avec_categorie(taches, nouvelle_tache, categorie):
    tache = {"nom": nouvelle_tache, "complet": False, "categorie": categorie}
    taches.append(tache)
    print(f"Tâche ajoutée : {nouvelle_tache} (Catégorie : {categorie})")

def supprimer_tache(taches, numero_tache):
    if numero_tache >= 1 and numero_tache <= len(taches):
        tache_supprimee = taches.pop(numero_tache - 1)
        print(f"Tâche supprimée : {tache_supprimee['nom']}")
    else:
        print("Numéro de tâche invalide")

nom_fichier = "taches.json"
taches = []

try:
    with open(nom_fichier, 'r') as fichier:
        taches = json.load(fichier)
except FileNotFoundError:
    taches = []

while True:
    print("\nOptions :")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Ajouter une tâche avec date d'échéance")
    print("4. Ajouter une tâche avec catégorie")
    print("5. Supprimer une tâche")
    print("6. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        afficher_taches(taches)
    elif choix == "2":
        nouvelle_tache = input("Entrez la nouvelle tâche : ")
        ajouter_tache(taches, nouvelle_tache)
    elif choix == "3":
        nouvelle_tache = input("Entrez la nouvelle tâche : ")
        date_str = input("Entrez la date d'échéance (YYYY-MM-DD) : ")
        try:
            date_echeance = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            ajouter_tache_avec_date(taches, nouvelle_tache, date_echeance)
        except ValueError:
            print("Format de date invalide. Utilisez YYYY-MM-DD.")
    elif choix == "4":
        nouvelle_tache = input("Entrez la nouvelle tâche : ")
        categorie = input("Entrez la catégorie : ")
        ajouter_tache_avec_categorie(taches, nouvelle_tache, categorie)
    elif choix == "5":
        numero_tache = int(input("Entrez le numéro de la tâche à supprimer : "))
        supprimer_tache(taches, numero_tache)
    elif choix == "6":
        with open(nom_fichier, 'w') as fichier:
            json.dump(taches, fichier)
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
