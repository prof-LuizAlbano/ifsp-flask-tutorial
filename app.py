from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/listar")
def listar_contatos():
    return "<h1>Lista de Contatos</h1>"


@app.route("/adicionar")
def adicionar_contato():
    return "<h1>Adicionar Contato</h1>"


@app.route("/visualizar/<int:id_contato>")
def visualizar_contato(id_contato):
    return f"<h1>Visualizar Contato: {id_contato}</h1>"


@app.route("/editar/<int:id_contato>")
def editar_contato(id_contato):
    return f"<h1>Editar Contato: {id_contato}</h1>"


@app.route("/excluir/<int:id_contato>")
def excluir_contato(id_contato):
    return f"<h1>Excluir Contato: {id_contato}</h1>"