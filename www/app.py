

from http.client import responses
import os
from flask import Flask, jsonify, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'atividade'
app.config['MYSQL_DATABASE_HOST'] = '172.21.0.2'
mysql.init_app(app)

@app.route('/', methods=["GET"])
def main():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from usuario')
    data = cursor.fetchall()
    return render_template('listagem.html', data=data)

@app.route('/guardar', methods=["POST"])
def guardar():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']

    if nome and endereco and email:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into usuario (nome, email, endereco) values(%s, %s, %s)',
            (nome, email, endereco)
            )
        conn.commit()
    
    return render_template('sucesso.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port, debug=True)