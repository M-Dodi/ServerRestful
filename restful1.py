
import os
import psycopg2
import sys
from flask import Flask, jsonify, request
import json

print("Directory corrente:", os.getcwd())

# Dettagli connessione
host = "localhost"
port = "5432"
user = "utente"
password = "password"

# Connessione database
try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname="accademia",
        user="postgres",
        password="postgres"
    )

    print("Connessione al database avvenuta con successo")
except Exception as e:
    print(f"Errore durante la connessione al database: {e}")
    exit()

try:
    cursor = connection.cursor()
    print("Scegli un'opzione:")
    print("1: Visualizza tutte le persone")
    print("2: Visualizza cognomi distinti")
    print("3: Visualizza tipi di assenza distinti")
    

    # Chiedi all'utente di scegliere un'opzione
    scelta = input("Inserisci il numero dell'opzione desiderata: ")

    # Esegui la query in base alla scelta dell'utente
    if scelta == "1":
        cursor.execute("SELECT * FROM persona")
        file_name = 'tutte le persone.json'
    elif scelta == "2":
        cursor.execute("SELECT distinct cognome FROM persona")
        file_name = 'cognomi_distinti.json'
    elif scelta == "3":
        cursor.execute("SELECT distinct tipo FROM assenza")
        file_name = 'risultati3.json'
    else:
        print("Opzione non valida")
        cursor.close()
        connection.close()
        exit()

    # Recupera e stampa i risultati
    rows = cursor.fetchall()
    with open('risultati.json', 'w') as file:
        json.dump(rows, file, default=str)

    for row in rows:
        print(row)

except Exception as e:
    print(f"Errore durante l'esecuzione della query: {e}")

finally:
        # Chiudi il cursore e la connessione
    try:    
        cursor.close()
    except Exception as e:
        print(f"Errore durante la chiusura del cursore: {e}")

    try:
        connection.close()
    except Exception as e:
        print(f"Errore durante la chiusura della connessione: {e}")