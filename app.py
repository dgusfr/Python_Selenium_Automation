from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'       
app.config['MYSQL_PASSWORD'] = ''       
app.config['MYSQL_DB'] = 'cadastro_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    
    if not nome or not email or not telefone:
        return jsonify({"message": "Dados incompletos"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Cadastro realizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message": "Erro ao cadastrar"}), 500

if __name__ == '__main__':
    app.run(debug=True)
