import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
DB_NAME = "robo_espacial.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

@app.route('/leituras', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    timestamp = dados.get('timestamp', datetime.utcnow().isoformat() + "Z")
    temp = dados.get('temperatura_c')
    lum = dados.get('luminosidade')
    pres = dados.get('presenca')
    prob = dados.get('probabilidade_vida')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leituras (timestamp, temperatura_c, luminosidade, presenca, probabilidade_vida)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, temp, lum, pres, prob))
    conn.commit()
    conn.close()

    return jsonify({"status": "sucesso", "mensagem": "Dados registrados com sucesso"}), 201

@app.route('/leituras', methods=['GET'])
def consultar_dados():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leituras ORDER BY id DESC LIMIT 100')
    linhas = cursor.fetchall()
    conn.close()

    resultados = [{"id": l[0], "timestamp": l[1], "temperatura_c": l[2], "luminosidade": l[3], "presenca": l[4], "probabilidade_vida": l[5]} for l in linhas]
    return jsonify(resultados), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
