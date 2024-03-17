from flask import Flask, request, make_response
from datetime import datetime
import mysql.connector
import time

app = Flask(__name__)

# Global counter
counter = 0

def connect_to_mysql():
    max_retries = 5
    retry_interval = 5  # seconds

    for _ in range(max_retries):
        try:
            connection = mysql.connector.connect(host='mysql',
                                                 user='lior',
                                                 password='12345678',
                                                 port=3306,
                                                 database='db')
            print("Connected to MySQL server successfully.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL server: {err}")
            print(f"Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)

    print("Max retries reached. Exiting...")
    exit(1)

# MySQL connection
connection = connect_to_mysql()

@app.route('/')
def increment_counter():
    global counter
    counter += 1

    # Create a cookie
    response = make_response("Internal IP address: " + request.remote_addr)
    #response.set_cookie('internal_ip', value=request.remote_addr, max_age=300)

    # Record access log
    cursor = connection.cursor()
    sql = "INSERT INTO access_log (access_time, client_ip, internal_ip) VALUES (%s, %s, %s)"
    cursor.execute(sql, (datetime.now(), request.remote_addr, request.remote_addr))
    connection.commit()
    cursor.close()

    return response

@app.route('/showcount')
def show_counter():
    return "Global counter number: " + str(counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
