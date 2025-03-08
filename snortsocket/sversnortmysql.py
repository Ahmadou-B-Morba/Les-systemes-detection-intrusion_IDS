import asyncio
import mysql.connector
import re

# Variable pour stocker la dernière donnée reçue
last_data = None

# Fonction pour se connecter à la base de données MySQL
def connect_to_mysql():
    try:
        # Connectez-vous à MySQL en remplaçant les valeurs par les vôtres
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123@mo",
            database="basesnortt"
        )
        print("Connexion à MySQL réussie !")
        return conn
    except mysql.connector.Error as err:
        print("Erreur lors de la connexion à MySQL : ", err)
        return None

# Fonction pour extraire l'alerte et la prédiction
def extract_alert_and_prediction(data_str):
    # Expression régulière pour correspondre à la structure de la donnée
    match = re.match(r'^(.*) Prediction: (.*)$', data_str)
    if match:
        alert = match.group(1).strip()
        prediction_ml = match.group(2).strip()
        return alert, prediction_ml
    else:
        print("Failed to match alert data:", data_str)
        return None, None

async def handle_client(reader, writer):
    global last_data  # Permet d'accéder à la variable last_data définie en dehors de cette fonction
    addr = writer.get_extra_info('peername')
    print(f"Connexion de {addr}")

    try:
        while True:
            data = await reader.read(1000)
            if not data:
                break
            received_str = data.decode().strip()
            print(f'Reçu: {received_str!r}')

            alert, prediction_ml = extract_alert_and_prediction(received_str)

            # Vérifier si la donnée reçue est différente de la dernière donnée enregistrée
            if alert and prediction_ml and data != last_data:
                # Se connecter à MySQL
                mysql_connection = connect_to_mysql()

                if mysql_connection:
                    try:
                        # Créer un curseur pour exécuter des requêtes SQL
                        cursor = mysql_connection.cursor()

                        # Insérer les données dans MySQL
                        sql_query = "INSERT INTO tabless (alert, prediction_ml) VALUES (%s, %s)"
                        cursor.execute(sql_query, (alert, prediction_ml))
                        mysql_connection.commit()

                        # Fermer le curseur et la connexion à MySQL
                        cursor.close()
                        mysql_connection.close()

                        print("Données insérées dans MySQL avec succès.")
                    except mysql.connector.Error as err:
                        print(f"Erreur lors de l'insertion des données : {err}")

                # Mettre à jour la dernière donnée reçue
                last_data = data

    except Exception as e:
        print(f"Une erreur s'est produite avec le client {addr}: {e}")
    finally:
        print(f"Connexion fermée avec le client {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 12345)
    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
