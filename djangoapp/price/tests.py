from django.test import TestCase
# Create your tests here.
import jsonify
import psycopg2

def api(var):
    conn = psycopg2.connect(database = "pi_db", 
                        user = "pi_user", 
                        host= '127.0.0.1',
                        password = "projeto_integrador2",
                        port = 5432)
    
    
    cursor = conn.cursor()
    cursor.execute(f'SELECT {var} FROM price_pi_db;')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
api('currency')