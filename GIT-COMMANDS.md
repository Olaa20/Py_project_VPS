# 🚀 Mémo Git – Young IT Lab

Voici les commandes essentielles pour travailler avec **Git** et **GitHub** sur ton projet VPS + Blog + Monitoring.

---

## 🔹 Initialisation (une seule fois)
```bash
git init
git remote add origin git@github.com:TonUser/MonRepo.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main

## 🔹 Workflow quotidien
## Vérifier l’état :

```bash
git status

##Ajouter les fichiers modifiés :

git add .

# ou fichier par fichier :
git add app.py templates/index.html


##  Commit :

git commit -m "Message clair des changements"


## Envoyer sur GitHub :

git push

## 🔹 Mettre à jour depuis GitHub
git pull

## 🔹 Historique & navigation

## Voir l’historique :

git log --oneline --graph --decorate --all


## Nouvelle branche :

git checkout -b dev

## Changer de branche :

git checkout main

## Fusionner une branche :

git merge dev