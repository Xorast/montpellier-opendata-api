**MODA**<br>Montpellier Open Data Api
--------------------------

# Introduction

## Problematique

La ville de Montpellier met a disposition un certain nombre de donnees. Ces donnees sous disponibles sous forme de fichiers (csv) sur le site [data.montpellier3m.fr/](https://data.montpellier3m.fr/). Cette forme limite leur utilisation par des applications web.

## Objectif

Rendre ces donnees accessibles via un API pour faciliter leur exploitation.

## Perimetres

Dans un premier temps, un prototype sera mis au point pour les donnees de l'[offre de transport TAM en temps reel](https://data.montpellier3m.fr/dataset/offre-de-transport-tam-en-temps-reel).

Si le prototype est concluant, d'autre jeu de donnees seront ajoutee progressivement jusqu'a couvrir l'ensemble des jeux de donnees mise a disposition par la ville.

# Architecture

## Recuperation des donnees

Le jeu de donnees `TAM_MMM_TpsReel.csv` est mis a jour toute les minutes sur le server de la ville ([ici](https://data.montpellier3m.fr/dataset/offre-de-transport-tam-en-temps-reel/resource/e37afbf0-0156-439e-9abe-1a2c84cc33d8)).

Un process :
- surveille la mise a jour de celui-ci
- telecharge le fichier si mis a jour
- envoie les nouvelles donnees a l'API  

> Technologies
> - Bash script

## API

Les donnees sont rendues disponibles par un RESTful API.

L'ERD (schema de la base de donnees) se trouve [ici](https://app.lucidchart.com/invitations/accept/a2c391d7-6e09-429f-82f3-5fb7ea95857d).

> Technologies
> - DjangoREST

# Developpements possibles
- Login features
- Couvrir d'autres jeux de donnees

# Auteur
- pangur@tutanota.com