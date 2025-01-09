from flask import Flask

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