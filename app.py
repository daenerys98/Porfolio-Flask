from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contatos')
def contatos():
     return render_template('contatos.html')

if __name__ == "__main__":
    app.run (debug=True)