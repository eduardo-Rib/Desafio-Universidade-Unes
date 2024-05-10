from flask import Flask, render_template
app = Flask(__name__)


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
