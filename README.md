🛡️ Système de Détection d’Intrusions basé sur l’Apprentissage Automatique
📌 Présentation du projet
Ce projet de fin d’études consiste à concevoir et implémenter un système de détection d’intrusions (IDS) combinant des outils de sécurité reconnus et des modèles d’apprentissage automatique, afin de renforcer la protection des réseaux informatiques contre les cyberattaques.

Le système permet de collecter, analyser et visualiser les alertes de sécurité issues à la fois :

D’un NIDS (Network-based IDS) pour la surveillance du trafic réseau.

D’un HIDS (Host-based IDS) pour la surveillance des hôtes.

L’objectif est d’offrir une détection plus intelligente, adaptative et efficace, capable d’identifier aussi bien des attaques connues que des comportements anormaux.

🎯 Objectifs
Comprendre les fondements de la cybersécurité et des systèmes IDS.

Mettre en œuvre un NIDS et un HIDS dans un environnement réel.

Exploiter des algorithmes de Machine Learning pour améliorer la détection des intrusions.

Développer une interface web intuitive pour la visualisation et l’analyse des alertes.

Comparer les résultats des approches traditionnelles et basées sur l’apprentissage automatique.

🧠 Approche adoptée
Le projet repose sur une architecture hybride combinant :

SNORT pour la détection réseau (NIDS).

OSSEC pour la détection côté hôte (HIDS).

Des modèles d’apprentissage automatique (Random Forest, SVM, Deep Learning).

Une application web développée avec Django pour centraliser et visualiser les données.

Les données collectées sont prétraitées, analysées et utilisées pour entraîner des modèles capables de prédire et classifier les activités malveillantes.

🧩 Fonctionnalités principales
Authentification des utilisateurs.

Configuration de l’IDS.

Visualisation des alertes NIDS et HIDS.

Tableaux de bord interactifs.

Graphiques d’analyse (priorité, type d’attaque, protocole, évolution temporelle).

Comparaison des performances des modèles ML.

🛠️ Technologies utilisées
🔐 Sécurité & Réseau
SNORT | OSSEC

Nmap / Zenmap | Metasploit | Wireshark

💻 Développement
Backend : Python, Django

Frontend : HTML, CSS, JavaScript, Bootstrap

Base de données : SQL

🤖 Machine Learning
Random Forest

Support Vector Machine (SVM)

Deep Learning

🖥️ Architecture générale
Le système repose sur un flux de données structuré :

Collecte des alertes depuis SNORT et OSSEC.

Stockage centralisé dans une base de données.

Traitement intelligent via des modèles ML.

Interface web pour l’analyse et la prise de décision.

📊 Résultats obtenus
Les expérimentations montrent que :

L’intégration du Machine Learning améliore la détection des intrusions.

Les faux positifs sont réduits.

Le système est plus adaptatif face aux nouvelles attaques.

La visualisation facilite l’analyse et la compréhension des menaces.

🚀 Perspectives
Intégration en temps réel dans un environnement de production.

Ajout d’un système de réponse automatique aux incidents.

Enrichissement des jeux de données d’entraînement.

Déploiement sous forme de SIEM léger.

👨‍🎓 Auteurs
Ahmadou Baba MORBA

Hamid Saleh OUMAR

Encadré par :

Mme Fetjah Leila – Faculté des Sciences Aïn Chock

📄 Contexte académique
Projet de Fin d’Études

Licence Sciences Mathématiques et Informatique – Option Réseaux

Année universitaire : 2022 / 2023
