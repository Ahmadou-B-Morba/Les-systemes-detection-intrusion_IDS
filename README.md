# Système de Détection d’Intrusions basé sur l’Apprentissage Automatique

## Présentation générale
Ce projet s’inscrit dans le cadre d’un **Projet de Fin d’Études (PFE)** et porte sur le **développement d’un système de détection d’intrusions (IDS)** combinant des techniques classiques de cybersécurité et des **méthodes d’apprentissage automatique**.
Face à la multiplication et à la sophistication des cyberattaques, les solutions de sécurité traditionnelles montrent certaines limites, notamment en matière d’adaptabilité. Ce projet propose une approche hybride visant à **améliorer la détection des intrusions réseau et hôte**, tout en facilitant l’analyse des alertes grâce à une **interface web centralisée**.

## Objectifs du projet
L’objectif principal est de concevoir un IDS capable de détecter efficacement des comportements malveillants sur un réseau informatique. Plus précisément, le projet vise à :

- Comprendre les principes fondamentaux de la **cybersécurité** et des systèmes IDS  
- Mettre en œuvre un **NIDS** et un **HIDS** dans un environnement réel  
- Exploiter le **Machine Learning** pour améliorer la précision de la détection  
- Réduire les faux positifs et les faux négatifs  
- Fournir une **interface graphique claire** pour la visualisation et l’analyse des alertes  

## Principe de fonctionnement
Le système repose sur une **architecture hybride** :

- **SNORT** est utilisé comme système de détection d’intrusions réseau (NIDS) afin d’analyser le trafic et identifier des signatures d’attaques connues.
- **OSSEC** est déployé comme système de détection d’intrusions hôte (HIDS) pour surveiller l’intégrité des fichiers, les journaux et les activités système.
- Les alertes collectées sont stockées dans une base de données et analysées à l’aide de **modèles d’apprentissage automatique**.
- Une **application web développée avec Django** permet d’afficher, filtrer et analyser les résultats via des tableaux de bord interactifs.

Cette approche permet de combiner **détection par signatures**, **analyse comportementale** et **apprentissage automatique**.

## Fonctionnalités principales
- Authentification des utilisateurs  
- Configuration du système IDS  
- Visualisation des alertes du **NIDS (SNORT)**  
- Visualisation des alertes du **HIDS (OSSEC)**  
- Tableaux de bord interactifs  
- Graphiques statistiques (types d’attaques, priorités, protocoles, évolution temporelle)  
- Analyse des prédictions issues des modèles de Machine Learning  

## Technologies et outils utilisés

### Cybersécurité & Réseaux
- SNORT  
- OSSEC  
- Nmap / Zenmap  
- Metasploit  
- Wireshark  

### Développement
- **Backend** : Python, Django  
- **Frontend** : HTML, CSS, JavaScript, Bootstrap  
- **Base de données** : SQL  

### Apprentissage automatique
- Random Forest  
- Support Vector Machine (SVM)  
- Deep Learning  

## Architecture du système
Le système est organisé autour de plusieurs composants :

1. **Collecte des données** depuis SNORT et OSSEC  
2. **Stockage centralisé** des alertes dans une base de données  
3. **Traitement et classification** à l’aide des modèles ML  
4. **Visualisation** via une interface web intuitive  
Cette architecture facilite la supervision de la sécurité et l’aide à la prise de décision.

## Résultats et analyse

Les expérimentations réalisées montrent que l’intégration du **Machine Learning** permet :

- une meilleure détection des comportements anormaux,  
- une réduction significative des faux positifs,  
- une meilleure adaptabilité face aux nouvelles attaques,  
- une analyse plus claire grâce aux graphiques et tableaux de bord.

## Perspectives d’amélioration
Plusieurs évolutions sont envisageables :

- Détection et analyse en **temps réel**  
- Ajout de mécanismes de **réponse automatique aux incidents**  
- Enrichissement des jeux de données d’apprentissage  
- Intégration dans une solution de type **SIEM**  
- Déploiement en environnement de production  

## Auteurs
- **Ahmadou Baba MORBA**  
- **Hamid Saleh OUMAR**

Encadré par :  
**Mme Fetjah Leila**  
Faculté des Sciences Aïn Chock – Casablanca
