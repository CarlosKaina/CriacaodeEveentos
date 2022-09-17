from flask import Flask,jsonify

app = Flask(__name__)

#construir as funcionalidades
@app.route('/')
def homepage():
    return 'A API esta no ar'

@app.route('/pegarvendas')
def pegarvendas():
    return 'teste_teste'

#rodar a nossa api
app.run(host='0.0.0.0')

