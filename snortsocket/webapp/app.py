from flask import Flask, render_template, jsonify
import mysql.connector
import asyncio

app = Flask(__name__)

last_data = None

def connect_to_mysql():
    try:
        # Connect to MySQL using your credentials
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123@mo",
            database="basesnort"
        )
        print("Connected to MySQL successfully!")
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL: ", err)
        return None

async def tcp_echo_client():
    global last_data

    while True:
        try:
            # Your TCP client code goes here to receive data from the server
            # For demonstration purposes, let's assume you receive some alert data
            data = "Alert: Intrusion detected!"

            # Check if the received data is different from the last data
            if data != last_data:
                # Connect to MySQL
                mysql_connection = connect_to_mysql()

                if mysql_connection:
                    # Create a cursor to execute SQL queries
                    cursor = mysql_connection.cursor()

                    # Insert the data into MySQL
                    sql_query = "INSERT INTO tablesnort (alert_info) VALUES (%s)"
                    cursor.execute(sql_query, (data,))
                    mysql_connection.commit()

                    # Close the cursor and MySQL connection
                    cursor.close()
                    mysql_connection.close()

                    print("Data inserted into MySQL successfully.")

                    # Update the last_data variable
                    last_data = data

            await asyncio.sleep(1)
        except Exception as e:
            print("An error occurred: ", e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts')
def get_alerts():
    try:
        # Connect to MySQL
        mysql_connection = connect_to_mysql()

        if mysql_connection:
            # Create a cursor to execute SQL queries
            cursor = mysql_connection.cursor()

            # Fetch alerts from the database
            cursor.execute("SELECT alert_info FROM tablesnort")
            alerts = [row[0] for row in cursor.fetchall()]

            # Close the cursor and MySQL connection
            cursor.close()
            mysql_connection.close()

            return jsonify(alerts)
        else:
            return jsonify({"error": "Failed to connect to MySQL database"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(tcp_echo_client())
    app.run(debug=True, host='127.0.0.1', port=5000)
