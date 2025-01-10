from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/listar")
def listar_contatos():
    return render_template("listar-contatos.html")


@app.route("/adicionar", methods=['POST', 'GET'])
def adicionar_contato():
    if request.method == 'POST':
        #Aqui iremos tratar os dados e salvá-los no banco de dados.
        pass

    return render_template("formulario-contato.html")


@app.route("/visualizar/<int:id_contato>")
def visualizar_contato(id_contato):
    return render_template("visualizar-contato.html")


@app.route("/editar/<int:id_contato>", methods=['POST', 'GET'])
def editar_contato(id_contato):
    if request.method == 'POST':
        #Aqui iremos tratar os dados e salvá-los no banco de dados.
        pass
    
    return render_template("formulario-contato.html")


@app.route("/excluir/<int:id_contato>")
def excluir_contato(id_contato):
    return f"<h1>Excluir Contato: {id_contato}</h1>"