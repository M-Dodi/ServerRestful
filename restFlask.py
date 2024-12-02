from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Dettagli connessione
host = "localhost"
port = "5432"
user = "postgres"
password = "postgres"
dbname = "accademia"

# Connessione database
def get_db_connection():
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    return conn

@app.route('/menu', methods=['GET'])
def menu():
    scelta = request.args.get('scelta')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if scelta == "1":
        cursor.execute("SELECT * FROM persona")
        result = cursor.fetchall()
    elif scelta == "2":
        cursor.execute("SELECT DISTINCT cognome FROM persona")
        result = cursor.fetchall()
    elif scelta == "3":
        cursor.execute("SELECT DISTINCT tipo FROM assenza")
        result = cursor.fetchall()
    else:
        result = {"error": "Opzione non valida"}
    
    cursor.close()
    conn.close()
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Cambia la porta se necessario