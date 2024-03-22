# Hackathon 2024 - Machine Learning II

## Contexte
Un four est utilisé pour produire de l’énergie en incinérant des déchets. L’objectif de ce Hackathon
est de construire un prédicteur pour la variable **Yield**.

## Ressources

A votre disposition, vous avez un historique pour 36 variables. Chaque point de cet historique décrit l’état du four.

Vous devez mettre en œuvre les connaissances acquises lors de vos cours pour réaliser un modèle **réseau de neurones** en python qui permette de prédire le rendement, Yield, du four..

Les données d'entraînement sont disponibles sur le moodle du cours Machine Learning II dans la rubrique Hackathon.

Un autre jeu de données de test ne contenant pas le rendement est disponible. C’est sur ces points là que vous devrez appliquer votre modèle afin de trouver le rendement manquant et sur lequel votre modèle sera évalué. Le yield du jeu de données de test vous est inconnu.

## Rendu
1. Vous devrez rédiger un document présentant votre travail :
décrivez la démarche suivie motivez les choix que vous avez fait, expliquez le pipeline qui vous a servi à réaliser le modèle retenu.
2. Vous devez exporter une liste de rendement correspondant aux données du dataset de test.

`rendement.txt` :

```
1.11
2.11
…
99.99
```
3. Vous devez fournir un zip du code d'entraînement et d'évaluation.


## Evaluation

L’évaluation se fera à 50% sur le rapport, et à 50% la MSE (Mean Squared Error) des points manquants. Les pourcentages peuvent évoluer selon le succès au Hackathon.