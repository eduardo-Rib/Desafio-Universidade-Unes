from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#https://github.com/jeancosta4/to-do-list/blob/main/app.py

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'dbunes'
mysql = MySQL(app)


# Rota para adicionar uma nova duvida
@app.route('/include', methods=['POST', 'GET'])
def Include():
    if request.method == 'POST':
        nome = request.form['fnome']
        email = request.form['femail']
        descricao = request.form['fdescricao']
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO duvidas (nome, email, descricao) VALUES (%s, %s, %s)", (nome, email, descricao))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('contatos'))

@app.route('/duvidas')
def duvidas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM duvidas")
    duvidas = cur.fetchall()
    cur.close()
    return render_template('duvidas.html', duvidas=duvidas)
     



#Rotas das paginas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contato')
def contatos():
    return render_template('contatos.html')


@app.route('/campus1')
def unidade1():
    return render_template('unidade1.html')

@app.route('/campus2')
def unidade2():
    return render_template('unidade2.html')

@app.route('/campus3')
def unidade3():
     return render_template('unidade3.html')
       
if __name__ == "__main__":
    app.run(debug=True)
