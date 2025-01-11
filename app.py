from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from db import DB

app = Flask(__name__)
app.secret_key = b'\xa0\xdd\x8b\xe05\x00\tP\xb7\x94_\xe9'

@app.route("/")
@app.route("/listar")
def listar_contatos():
    conn = DB()
    rows = conn.read("SELECT id, nome, telefone, data_nascimento, email FROM contatos ORDER BY nome")
    conn.close()
    return render_template("listar-contatos.html", rows=rows)


@app.route("/adicionar", methods=['POST', 'GET'])
def adicionar_contato():
    if request.method == 'POST':
        sql = "INSERT INTO contatos (nome, telefone, data_nascimento, email) VALUES (?, ?, ?, ?)"

        conn = DB()
        conn.write(sql, (
            request.form['nome'], 
            request.form['telefone'], 
            request.form['data_nascimento'],
            request.form['email']
        ))
        conn.close()

        flash("Contato adicionado com sucesso!")
        return redirect(url_for('listar_contatos'))

    return render_template("formulario-contato.html", title="Adicionar Contato", dados=None)


@app.route("/visualizar/<int:id_contato>")
def visualizar_contato(id_contato):
    conn = DB()
    #Recuperamos os dados do registro a ser editado
    record = conn.read_one(f"SELECT * FROM contatos WHERE id={id_contato}")
    conn.close()

    return render_template("visualizar-contato.html", dados=record)


@app.route("/editar/<int:id_contato>", methods=['POST', 'GET'])
def editar_contato(id_contato):
    conn = DB()

    #Recuperamos os dados do registro a ser editado
    record = conn.read_one(f"SELECT * FROM contatos WHERE id={id_contato}")

    if request.method == 'POST':
        conn.write("UPDATE contatos SET nome=?, telefone=?, data_nascimento=?, email=? WHERE id=?", (
            request.form['nome'],
            request.form['telefone'],
            request.form['data_nascimento'],
            request.form['email'], 
            id_contato
        ))

        flash("Contato editado com sucesso!")
        return redirect(url_for('listar_contatos'))

    conn.close()
    return render_template("formulario-contato.html", title="Editar Contato", dados=record)


@app.route("/excluir/<int:id_contato>")
def excluir_contato(id_contato):
    if id_contato > 0:
        conn = DB()
        conn.write("DELETE FROM contatos WHERE id=?", (id_contato, ))
        conn.close
        flash("Contato removido com sucesso!")
        return redirect(url_for('listar_contatos'))

    flash("Contato não removido!")
    return redirect(url_for('listar_contatos'))