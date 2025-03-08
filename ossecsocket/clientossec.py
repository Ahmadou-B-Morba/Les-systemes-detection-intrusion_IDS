import socket
import json
import time
import pandas as pd
import joblib
from datetime import datetime

# Adresse et port du serveur
host = '192.168.13.1'  # Adresse IP du serveur
port = 12345  # Port utilisé par le serveur

# Chemin vers le fichier de logs
log_file_path = "/var/ossec/logs/alerts/alerts.json"

# Charger le modèle
pipeline = joblib.load('pipeline_model.pkl')

# Créer un objet de socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au serveur
client_socket.connect((host, port))

print("Connecté au serveur.")

# Position de la fin du fichier
end_position = None

# Fonction pour extraire les attributs requis avec leur valeur ou None si manquant
def extract_attribute(obj, attr):
    if isinstance(obj, dict):
        return obj.get(attr, None)
    return None

# Liste des colonnes requises par le modèle
required_columns = [
    'timestamp', 'rule.level', 'rule.id', 'rule.groups', 'hostname',
    'agent_name', 'source_ID', 'syslog', 'apparmor', 'ids', 'sudo', 'syscheck',
    'year', 'pam', 'month', 'errors', 'authentication_success', 'day', 'ossec',
    'hour', 'day_of_week', 'local'
]

# Boucle continue pour surveiller les nouveaux éléments
while True:
    # Ouvrir le fichier de logs en mode lecture
    with open(log_file_path, 'r') as file:
        # Se positionner à la fin du fichier
        file.seek(0, 2)
        
        # Récupérer la position de la fin du fichier
        current_end_position = file.tell()
        
        # Vérifier s'il y a de nouvelles données depuis la dernière lecture
        if end_position is not None and current_end_position > end_position:
            # Lire les nouvelles lignes ajoutées au fichier depuis la dernière lecture
            file.seek(end_position)
            new_lines = file.readlines()
            
            for line in new_lines:
                # Convertir chaque ligne en JSON
                try:
                    obj = json.loads(line)
                    
                    # Extraire les attributs requis avec leur valeur ou None si manquant
                    timestamp = extract_attribute(obj, 'timestamp')
                    level = extract_attribute(obj.get('rule', {}), 'level')
                    rule_id = extract_attribute(obj.get('rule', {}), 'sidid')
                    rule_groups = extract_attribute(obj.get('rule', {}), 'groups')
                    hostname = extract_attribute(obj, 'hostname')
                    agent_name = extract_attribute(obj, 'agent_name')
                    source_ID = extract_attribute(obj, 'id')
                    
                    # Créer un dictionnaire avec la structure des données pour la prédiction
                    data_structure = {
                        'timestamp': timestamp,
                        'rule.level': level,
                        'rule.id': rule_id,
                        'rule.groups': rule_groups,
                        'hostname': hostname,
                        'agent_name': agent_name,
                        'source_ID': source_ID
                    }

                    # Ajouter les colonnes manquantes avec des valeurs par défaut
                    for column in required_columns:
                        if column not in data_structure:
                            data_structure[column] = None

                    # Prétraiter les données pour la prédiction
                    df = pd.DataFrame([data_structure])
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                    df['year'] = df['timestamp'].dt.year
                    df['month'] = df['timestamp'].dt.month
                    df['day'] = df['timestamp'].dt.day
                    df['hour'] = df['timestamp'].dt.hour
                    df['day_of_week'] = df['timestamp'].dt.dayofweek
                    df['timestamp'] = df['timestamp'].apply(lambda x: x.timestamp())

                    # Faire la prédiction avec le modèle
                    prediction_ml = pipeline.predict(df)
                    
                    # Ajouter la prédiction aux données originales
                    obj['prediction_ml'] = prediction_ml[0]
                    
                    # Convertir l'alerte complète avec la prédiction en JSON et l'envoyer au serveur
                    json_data = json.dumps(obj)
                    print(f"Données envoyées au serveur: {json_data}")
                    client_socket.send(json_data.encode('utf-8'))
                    
                except json.JSONDecodeError as e:
                    print(f"Erreur de lecture des données JSON: {e}")
                except Exception as e:
                    print(f"Erreur lors du traitement: {e}")

        # Mettre à jour la position de la fin du fichier
        end_position = current_end_position
    
    # Attendre un court instant avant de vérifier à nouveau le fichier
    time.sleep(0.1)

# Fermer la connexion
client_socket.close()
