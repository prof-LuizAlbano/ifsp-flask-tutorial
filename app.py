from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/caminho")
def nome_funcao():
    return "Aqui entrará o código HTML da tela"


@app.route("/ver/produto/<int:id>")
def ver_produto(id):
    return f"O ID deste produto é {id}"


@app.route("/exemplo-template")
def exemplo_template():
    return render_template("exemplo.html")

@app.route("/exemplo-template-2")
def exemplo_template2():
    return render_template("exemplo2.html", teste="Este é um valor que foi repassado ao template")