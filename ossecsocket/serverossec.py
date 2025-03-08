import socket
import mysql.connector
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def insert_data(cursor, db, data):
    try:
        sql = """
        INSERT INTO tableossec (
            id, rule_level, rule_comment, rule_sidid, rule_firedtimes, rule_groups,
            location, hostname, program_name, decoder_desc, agent_name, timestamp, logfile, prediction_ml
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            data.get("id", None),
            data["rule"].get("level", None),
            data["rule"].get("comment", None),
            data["rule"].get("sidid", None),
            data["rule"].get("firedtimes", None),
            ",".join(data["rule"].get("groups", [])),
            data.get("location", None),
            data.get("hostname", None),
            data.get("program_name", None),
            data.get("decoder_desc", {}).get("name", None),
            data.get("agent_name", None),
            format_timestamp(data.get("timestamp", None)),
            data.get("logfile", None),
            data.get("prediction_ml", None)
        ))
        db.commit()
        logging.info("Données insérées dans la base de données.")
    except mysql.connector.Error as err:
        logging.error("Erreur lors de l'insertion des données : %s", err)

def format_timestamp(timestamp_str):
    try:
        timestamp = datetime.strptime(timestamp_str, '%Y %b %d %H:%M:%S')
        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_timestamp
    except ValueError:
        logging.error("Format de timestamp incorrect : %s", timestamp_str)
        return None

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123@mo",
        database="projectpfe"
    )
    cursor = db.cursor()
    logging.info("Connexion à la base de données réussie.")
except mysql.connector.Error as err:
    logging.error("Erreur de connexion à la base de données : %s", err)
    exit(1)

host = '0.0.0.0'
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

logging.info("En attente de connexion...")

client_socket, client_address = server_socket.accept()
logging.info("Connexion établie avec %s", client_address)

BUFFER_SIZE = 4096

while True:
    try:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        log_data = json.loads(data.decode('utf-8'))
        logging.info("Client: %s", log_data)

        insert_data(cursor, db, log_data)
    except Exception as e:
        logging.error("Une erreur s'est produite : %s", e)

client_socket.close()
server_socket.close()
