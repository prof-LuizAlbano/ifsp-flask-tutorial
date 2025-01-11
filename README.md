# Tutorial Flask - Programação Web
Tutorial sobre o uso do framework Flask / Python elaborado para a disciplina de Programação Web, do curso Técnico Integrado em Redes de Computadores do IFSP Campus Pirituba.


**Autores:** [Luiz Albano](https://github.com/prof-LuizAlbano) e [Renato  Montanher](https://github.com/RenatoMontanher).

São Paulo, 2025. Versão: 1.0 (Janeiro/2025).

## Introdução
Este repositório tem o propósito de reunir textos e exemplos em forma de tutorial, sendo elaborado para a disciplina Programação Web do curso Técnico em Redes de Computadores do Instituto Federal de São Paulo (IFSP) - Campus Pirituba. Seu principal objetivo é demonstrar o passo a passo do desenvolvimento de uma pequena aplicação web baseada no framework Flask/Python, envolvendo a utilização de templates, formulários e manipulação de dados em banco de dados.

A aplicação de exemplo trata-se de uma agenda de contatos, com funcionalidades para visualização, inclusão, edição e exclusão de contatos e utiliza-se de uma tabela de dados em SQLite.

## 1. Criando a aplicação Flask
Para demonstração da aplicação de exemplo utilizamos a versão 3.13 do Python, em ambiente virtual (virtualenv), esta é uma boa prática para evitarmos conflitos de bibliotecas e recursos com outras aplicações Python instaladas em um computador.

Por questões práticas não iremos demonstrar a instalação do Python. Mas espera-se que exista uma instalação do Python no computador em que você for trabalhar.

O **virtualenv** é um recurso do Python que cria um ambiente virtual isolado para cada projeto. Dentro deste ambiente, fazemos a instalação das bibliotecas necessárias a um projeto, como a biblioteca Flask.
<br>

**Instalando o virtualenv**

Para instalar o virtualenv no Windows, abra uma janela de terminal e digite o seguinte comando:

`pip install virtualenv`


<br>


**Criação do diretório da aplicação**

Após a instalação da biblioteca virtualenv ou se ela já tiver sido instalada em seu computador, prossiga para a criação do diretório da aplicação.

No local em que preferir em seu computador, crie um diretório (pasta) onde ficarão armazenados os arquivos de sua aplicação.

Para o nosso exemplo vamos nomear o diretório da aplicação como: ifsp-flask-tutorial.

`mkdir ifsp-flask-tutorial`
<br>

**Configuração do ambiente virtual no diretório da aplicação**

O próximo passo é criarmos um ambiente virtual no diretório da aplicação. Navegue até o diretório da aplicação e execute o comando abaixo:

`python -m venv .venv`
<br>

**.venv** é o diretório que será criado para salvar os arquivos necessários como o interpretador do Python, bibliotecas, etc. Nota importante: este diretório não deve ser enviado nas entregas de atividades.

Após a configuração do ambiente virtual, toda vez que for iniciar sua aplicação, você deverá iniciar o ambiente. Isto é realizado através do comando abaixo:

`.\.venv\Scripts\activate`
<br>

A partir daqui temos tudo pronto para iniciarmos o projeto. Se tudo estiver sido configurado de maneira correta, você deverá ver o prefixo (.venv) em seu terminal.

Uma vez ativado o ambiente virtual, quando desejarmos interromper o ambiente o seguinte comando deverá ser executado:

`deactivate`
<br>

**Instalação do Flask**

Realizadas as configurações iniciais do projeto, o próximo passo é realizar a instalação da biblioteca Flask.

Execute o comando a seguir para instalar o Flask em seu ambiente virtual:

`pip install Flask`
<br>


**Criando uma aplicação para teste**

Para testarmos o processo de instalação e configuração do ambiente de desenvolvimento, vamos criar uma pequena rota que imprime um simples conteúdo HTML.

No diretório raíz de sua aplicação, crie um arquivo chamado **`app.py`** e cole o código abaixo:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Entendendo o código acima:

1. Na primeira linha importamos a biblioteca Flask (que foi anteriormente instalada) 
2. A segunda linha de comando cria uma instância de objeto da classe Flask, que será nossa aplicação WSGI (Web Server Gateway Interface, em uma breve explicação, nossa porta de entrada de requisições). O primeiro argumento é o nome do módulo ou pacote do aplicativo. `__name__` é um atalho conveniente para isso que é apropriado para a maioria dos casos. Isso é necessário para que o Flask saiba onde procurar recursos como modelos e arquivos estáticos.
3. Em seguida declaramos um decorator do Python, que é uma declaração que modifica ou estende o comportamento de uma função ou método. O decorator route() determina qual URL deve acionar a função.
4. Definimos uma função que retorna a mensagem que queremos que seja exibido no navegador do usuário. O tipo de conteúdo padrão é o HTML, então o conteúdo da string retornado pela função será renderizado pelo navegador.

Para executarmos nossa aplicação, em uma tela de terminal com o cursor presente no diretório raíz da aplicação, execute o comando abaixo:

`flask –app [nome_arquivo] run –debug`
<br>

No comando acima substitua **[nome_arquivo]** pelo nome do arquivo inicial de sua aplicação, sem sua extensão. Em nosso tutorial, o nome do arquivo é app. Também adicionamos ao final do comando o parâmetro **`–debug`** para que nosso código seja recarregado automaticamente quando houver mudanças. Isto facilita durante o processo de desenvolvimento, pois não precisamos ter que parar o servidor e reiniciar novamente em cada mudança de arquivo.

## 2. Sobre a aplicação de exemplo

Para fins didáticos, iremos desenvolver uma pequena aplicação do tipo “Agenda de Contatos”. Nesta seção descreveremos as principais funcionalidades para melhor compreensão dos passos de desenvolvimento apresentados nas seções seguintes.

Nossa Agenda de Contatos terá as seguintes funcionalidades:
* **Lista de contatos:** página inicial da aplicação. Deverá listar, em ordem alfabética, a lista de contatos cadastradas em nossa agenda, exibindo o nome do contato, seu telefone, data de nascimento e endereço de e-mail;
* **Adicionar contato:** deve apresentar um formulário contendo os seguintes campos: nome, telefone, data de nascimento e e-mail. Ao enviar os dados do formulário, nossa aplicação deve inserir uma nova entrada na tabela do banco de dados;
* **Editar contato:** a partir da lista de contatos, um usuário pode selecionar um cadastro para editar (atualizar) informações. Ao selecionar a edição de um contato, deve ser exibido um formulário (igual ao formulário de adição de contato), porém os campos devem estar preenchidos com os dados do contato que será atualizado. Ao enviar os dados do formulário, nossa aplicação deverá editar o respectivo registro na tabela do banco de dados;
* **Visualizar contato:** a partir da lista de contatos, um usuário pode selecionar um cadastro para visualizar suas informações. Ao selecionar a visualização de um contato, deve ser exibida uma página contendo as informações do contato selecionado;
* **Excluir contato:** a partir da lista de contatos, um usuário pode selecionar um cadastro para excluir de seus contatos. Ao selecionar um registro, a aplicação deve confirmar a exclusão, e se confirmada, o registro deverá ser excluído da tabela no banco de dados. Ao finalizar a exclusão, a lista de contatos deve ser exibida novamente, com a lista de contatos atualizada.
  
Para o desenvolvimento desta aplicação vamos criar um banco de dados baseado no SQLite. Prossiga com os passos abaixo para realizar a criação do banco de dados:

**Passo 1:** crie um diretório chamado **`db/`** dentro do diretório da aplicação.

**Passo 2:** no diretório **`db/`**, crie um arquivo chamado **`schema.sql`** e cole o código abaixo.
```
DROP TABLE IF EXISTS contatos;

CREATE TABLE contatos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(50) NOT NULL,
  telefone VARCHAR(20),
  data_nascimento DATE,
  email VARCHAR(100),
  data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

**Passo 3:** agora no diretório raíz da aplicação, crie um arquivo chamado **`init_db.py`** e cole o código abaixo.

```
import sqlite3

connection = sqlite3.connect('db/agenda.db')

with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()
```

**Passo 4:** em uma janela de terminal, com o cursor direcionado para o diretório raíz da aplicação execute o script criado no passo anterior com o interpretador do Python:

`python init_db.py`

Após realizar os passos acima sua aplicação deverá conter, dentro do diretório **`db/`**, um novo arquivo chamado **`agenda.db`**. Este arquivo armazenará os dados de nossa aplicação, armazenando os valores dentro da tabela contatos.

## 3. Organizando a aplicação

Manter uma boa estrutura e organização dos arquivos torna o projeto mais legível e de fácil manutenção. Desta forma apresentamos uma estrutura de arquivos e diretórios que utilizaremos neste tutorial.

```
|-- ifsp-flask-tutorial
|   +-- db
|   |   |-- agenda.db
|   |   |-- schema.sql
|   +-- static
|   |   +-- css
|   |   |   |-- <arquivos de estilos> 
|   |   +-- images
|   |   |   |-- <imagens> 
|   |   +-- js
|   |   |   |-- <scripts javascript> 
|   +-- templates
|   |   |-- <arquivos de template> 
|   |-- app.py
|   |-- init_db.py
```

* O diretório **ifsp-flask-tutorial** é o diretório de nossa aplicação.
* O diretório **db** contém dois arquivos, sendo o arquivo agenda.db nosso banco de dados e o arquivo schema.sql contendo as instruções SQL para criação da tabela contatos.
* O diretório **static** reúne os arquivos estáticos da aplicação que serão referenciados pelos códigos HTML. Dentro deste diretório, foram criados outros três diretórios, sendo eles:
    * **css:** para armazenar os arquivos de estilos utilizados pela aplicação
    * **images:** para armazenar as imagens
    * **js:** para armazenar os scripts em linguagem javascript, responsáveis pelo controle da interação e elementos HTML.
* O diretório **templates** irá abrigar os arquivos contendo códigos HTML que serão utilizados pela aplicação para a renderização dos conteúdos.
* No diretório raíz de nossa aplicação há dois arquivos Python:
    * **`app.py`**: nosso ponto de partida da aplicação, ontém os códigos já descritos na seção anterior;
    * **`init_db.py`**: script Python para criação do banco de dados. Deve ser executando apenas uma vez, antes do prosseguimento deste tutorial.


## 4. Rotas

As rotas são um conceito importante em um sistema web. Elas determinam a maneira de se chegar a um determinado lugar da aplicação. Se quisermos que os usuários acessem uma página de login, precisamos determinar uma rota para a página de login. Se precisarmos que um usuário chegue até a página de registro, teremos uma rota para ela e assim por diante. 

Podemos definir, basicamente, rotas de forma estática ou dinâmica.

Definimos uma rota da seguinte maneira:

```
@app.route("/caminho")
def nome_funcao():
    return "Aqui entrará o código HTML da tela"
```

* **@app.route:** notação utilizada para dizer que estamos criando uma rota. Dentro do parênteses dessa notação precisamos colocar o nome que daremos para ela. 
* **def nome_funcao:** cada rota ao ser acionada precisa ter uma def que executará as devidas ações.
  
**Rotas dinâmicas**

Um rota pode também pode receber parâmetros, que são valores dinâmicos. Em uma tela para exibição de um produto, podemos acessar as informações deste produto através da rota correspondente e um código correspondente ao produto, por exemplo.

Veja um exemplo de definição de uma rota dinâmica:

```
@app.route("/ver/produto/<int:id>")
def ver_produto(id):
    return f"O ID deste produto é {id}"
```

No exemplo anterior a página acessada teria a seguinte URL: `http://127.0.0.1:5000/ver/produto/123`.
Para adicionar criar uma rota dinâmica, basta adicionar uma seção **`<nome_varialvel>`** no nome da URL definida. A função que irá responder à rota deve declarar o **nome_variavel**, como um parâmetro. Opcionalmente a seção de variável pode declarar o tipo de argumento da seguinte maneira: **`<tipo:nome_variavel>`**.

Tipos de variáveis:
* string: (padrão) aceita qualquer texto sem barra
* int: aceita inteiros positivos
* float: aceita valores de ponto flutuante positivos
* path: como uma string, porém aceita barras
* uuid: aceita strings UUID

Para nosso tutorial vamos criar 5 (cinco) rotas. Vamos inserí-las no arquivo **`app.py`**. Por ora iremos apenas criar as rotas e ao longo deste tutorial, faremos as devidas alterações, incluindo as ações que nossa aplicação deverá realizar.

```
from flask import Flask

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
```

## 5. Templates

Todas as rotas são associadas a uma função que retorna o conteúdo do processamento. Retornar todo o código HTML dentro de uma função aumenta consideravelmente as linhas de código e dificulta a manutenção de um arquivo.

Uma boa prática é a utilização de templates.
Templates são arquivos estáticos que podem conter espaços (placeholders) para dados dinâmicos. Um arquivo de template é renderizado (processado) com dados específicos para produzir o documento final.

Estes arquivos, por padrão, são armazenados no diretório **templates/** de sua aplicação. Para melhorar a organização, dependendo do tamanho de sua aplicação, os arquivos também podem ser organizados em subdiretórios.

Os arquivos de template são arquivos HTML que podem conter espaços (placeholders) delimitados por:
* {{ }} - expressões que produzem saídas no documento, funcionando como um print do Python.
* {% %} - expressões de controle de fluxo ou funções (como if, for, etc). Este placeholder também é utilizado para comandos como **extends**, quando inserimos outro arquivo HTML que será estendido, e **block** para definirmos blocos de conteúdos que podem ser substituídos, em outros arquivos.

Para utilizarmos templates devemos adicionar a biblioteca **render_template**, que adiciona a função de mesmo nome que retorna o resultado do processamento do arquivo de template como um arquivo estático.

Vejamos um exemplo de uso:

```
from flask import render_template
@app.route("/exemplo-template")
def exemplo_template():
    return render_template("exemplo.html")
```

**Passando valores dinâmicos para um template**

```
from flask import render_template
@app.route("/exemplo-template-2")
def exemplo_template2():
    return render_template("exemplo2.html", teste="Este é um valor que foi repassado ao template")
```

No exemplo acima o valor exibido é o valor contido na variável **teste**, passada como argumento na função **render_template**. Para que o valor seja impresso na página, no arquivo de template é necessário inserir o nome da variável entre duas chaves:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask - Exemplo 01 do uso de templates</title>
</head>
<body>
    <h1>{{teste}}</h1>
</body>
</html>
```

**Templates do tutorial**

Para nosso tutorial vamos adotar o uso de templates. Para começarmos, vamos criar um arquivo chamado **`base.html`**. Lembrando que os arquivos de template devem ser salvos no diretório **`templates/`**. Este arquivo será uma página contendo o cabeçalho e rodapé da aplicação e também dois blocos:
* **page_title**: para definirmos o título da página
* **page_content**: para inserirmos a parte de conteúdo da página conforme a rota.

**Conteúdo do arquivo base.html:**

```
<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Luiz Albano and Renato Montanher">
    <title>Agenda de Contatos | {% block page_title %}Lista de Contatos{% endblock %}</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link href="static/css/agenda.css" rel="stylesheet">
</head>
<body>           
    <main>
        <div class="container py-4">
            <header class="pb-3 mb-4 border-bottom">
                <a href="/" class="d-flex align-items-center text-body-emphasis text-decoration-none">
                    <svg width="48px" height="48px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                        <title>contacts-solid</title>
                        <g id="Layer_2" data-name="Layer 2">
                          <g id="invisible_box" data-name="invisible box">
                            <rect width="48" height="48" fill="none"/>
                          </g>
                          <g id="Q3_icons" data-name="Q3 icons">
                            <g>
                              <path d="M14,31.7V34H28V31.7a15.3,15.3,0,0,0-14,0Z"/>
                              <circle cx="21" cy="17" r="3"/>
                              <path d="M36,3H6A2,2,0,0,0,4,5V43a2,2,0,0,0,2,2H36a2,2,0,0,0,2-2V5A2,2,0,0,0,36,3ZM21,10a7,7,0,1,1-7,7A7,7,0,0,1,21,10ZM32,36a2,2,0,0,1-2,2H12a2,2,0,0,1-2-2V29.4l.9-.6a19.6,19.6,0,0,1,20.2,0l.9.6Z"/>
                              <path d="M42,19H40V29h2a2,2,0,0,0,2-2V21A2,2,0,0,0,42,19Z"/>
                              <path d="M42,31H40V41h2a2,2,0,0,0,2-2V33A2,2,0,0,0,42,31Z"/>
                              <path d="M42,7H40V17h2a2,2,0,0,0,2-2V9A2,2,0,0,0,42,7Z"/>
                            </g>
                          </g>
                        </g>
                      </svg>

                    <span class="fs-4 ms-3 fw-bold">Agenda de Contatos</span>
                </a>
            </header>

            {% block page_content %}{% endblock %}

            <footer class="pt-3 mt-4 text-body-secondary border-top">
                &copy; IFSP - Técnico em Redes de Computadores: Programação Web - 2024/2025
            </footer>
        </div>
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="static/js/agenda.js"></script>
</body>
</html>
```

Vamos também construir os arquivos de template que utilizaremos nas rotas apresentadas anteriormente. Vamos começar com a rota inicial que faz a listagem dos contatos.

Crie um arquivo chamado **`listar-contatos.html`**. Neste arquivo vamos definir conteúdos para os blocos **page_title** e **page_content**, sendo este último, um bloco contendo os códigos HTML que exibem uma tabela contendo as informações dos contatos cadastrados (nesta primeira versão, temos apenas um exemplo e não criamos a interação com os dados) e um botão para adicionar um novo contato. 

No início do arquivo devemos importar o arquivo **`base.html`** através do comando **`{% extends 'base.html' %}`**. Este procedimento ocorrerá em todos os arquivos das demais rotas.

**Conteúdo do arquivo listar-contatos.html:**

```
{% extends 'base.html' %}

{% block page_title %}
Lista de Contatos
{% endblock %}

{% block page_content %}

<div class="container-fluid py-4">
    <div class="d-flex align-self-center">
        <h1>Lista de Contatos</h1>
        <a href="/adicionar" class="ms-auto py-3 btn btn-success fw-bold">[+] Adicionar Contato</a>
    </div>

    <div class="row py-5">
        <table class="table table-hover table-striped ">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Nome</th>
                    <th>Telefone</th>
                    <th>Data de Nascimento</th>
                    <th>E-mail</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>0</td>
                    <td>Nome do contato</td>
                    <td>(00) 0000-0000</td>
                    <td>00/00/0000</td>
                    <td>nome@provedor.com.br</td>
                    <td>
                        <a href="/visualizar/0" class="text-dark">Visualizar</a> |
                        <a href="/editar/0" class="text-dark">Editar</a> |
                        <a href="/excluir/0" class="text-danger delete-item">Excluir</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

</div>

{% endblock %}
```

**Conteúdo do arquivo visualizar-contato.html:**

```
{% extends 'base.html' %}

{% block page_title %}
Visualização de dados
{% endblock %}

{% block page_content %}

<div class="container-fluid py-4">
    <div class="d-flex align-self-center">
        <h1>Dados do Contato</h1>
        <a href="/listar" class="ms-auto py-3 btn btn-dark fw-bold">&lt;- Voltar</a>
    </div>

    <div class="row py-5">
        <table class="table table-hover table-striped ">
            <tbody>
                <tr>
                    <th width="200">#</th>
                    <td>0</td>
                </tr>
                <tr>
                    <th>Nome</th>
                    <td>Nome do contato</td>
                </tr>
                <tr>
                    <th>Telefone</th>
                    <td>(00) 0000-0000</td>
                </tr>
                <tr>
                    <th>Data de Nascimento</th>
                    <td>00/00/0000</td>
                </tr>
                <tr>
                    <th>E-mail</th>
                    <td>nome@provedor.com.br</td>
                </tr>
                <tr>
                    <th>Data de Cadastro</th>
                    <td>00/00/0000 00:00:00</td>
                </tr>
            </tbody>
        </table>

        <div class="d-flex">
            <a href="/editar/0" class="btn btn-success">Editar</a>
            <a href="/excluir/0" class="btn btn-danger ms-2 delete-item">Excluir</a>
            <a href="/listar" class="ms-auto btn btn-dark fw-bold">&lt;- Voltar</a>
        </div>
    </div>

</div>

{% endblock %}
```

**Conteúdo do arquivo formulario-contato.html:**

Este arquivo será utilizado tanto para a rota de adicionar, quanto para a rota de editar, pois se utilizam do mesmo formulário de campos. Ao longo do tutorial iremos explicar alguns detalhes deste formulário.

```
{% extends 'base.html' %}

{% block page_title %}
{{title}}
{% endblock %}

{% block page_content %}

<div class="container-fluid py-4">
    <div class="d-flex align-self-center">
        <h1>{{title}}</h1>
        <a href="/listar" class="ms-auto py-3 btn btn-dark fw-bold">&lt;- Voltar</a>
    </div>

    <div class="row py-5">
        <form action="" method="post">
            <div class="row mb-3">
                <label for="form_input_Nome" class="col-sm-2 col-form-label">Nome</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" id="form_input_Nome" required="required" name="nome" value="{{ dados['nome'] }}">
                </div>
            </div>

            <div class="row mb-3">
                <label for="form_input_Telefone" class="col-sm-2 col-form-label">Telefone</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control phone-mask" id="form_input_Telefone" name="telefone" required="required" value="{{ dados['telefone'] }}" placeholder="(XX) XXXXX-XXXX">
                </div>
            </div>

            <div class="row mb-3">
                <label for="form_input_DataNascimento" class="col-sm-2 col-form-label">Data de Nascimento</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control date-mask" id="form_input_DataNascimento" name="data_nascimento" required="required" value="{{ dados['data_nascimento'] }}" placeholder="DD/MM/YYYY">
                </div>
            </div>

            <div class="row mb-3">
                <label for="form_input_Email" class="col-sm-2 col-form-label">Email</label>
                <div class="col-sm-10">
                    <input type="email" class="form-control" id="form_input_Email" required="required" name="email" value="{{ dados['email'] }}">
                </div>
            </div>

            <div class="d-flex">
                <label class="col-sm-2 ms-1 col-form-label">&nbsp;</label>
                <button type="submit" class="btn btn-success">Salvar</button>
                <a href="/listar" class="ms-auto btn btn-dark fw-bold">&lt;- Voltar</a>
            </div>
        </form>
        
    </div>

</div>

{% endblock %}
```

## 6. Formulários e Requisições

Em aplicações web é essencial manipular as informações que um usuário envia ao servidor. O framework Flask fornece estas informações através de um objeto chamado **request**. 

Para utilizarmos é necessário a importação da biblioteca **request**:

`from flask import request`

No protocolo HTTP temos disponíveis alguns métodos para requisição dos dados, como HEAD, PUT, DELETE, GET e POST, sendo os dois últimos, os métodos que iremos utilizar em nosso exemplo. Uma explicação mais detalhada sobre os métodos HTTP pode ser encontrada em: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods

Em formulários, geralmente, utilizamos o método post para envio das informações. Neste método, basicamente, o navegador monta um pacote de requisição e insere os valores e variáveis no corpo deste pacote, que será recebido pelo servidor. Nossa aplicação, deverá receber estes dados e processá-los, para adicionar um novo usuário, ou editar os dados de um já existente.

Em uma função podemos obter o método de envio das informações, através do atributo **method**, presente no objeto **request**. Já os dados enviados por um formulário, que utilize o método POST podem ser acessados pelo atributo **form**.

Veja um exemplo a seguir:

```
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

No exemplo acima, a rota **`/login`** é configurada para aceitar requisições aos métodos POST e GET. A função destinada a esta rota, verifica se a requisição recebida é do tipo POST, e se verdadeira, confere os dados de login repassando à função **`valid_login`** os dados enviados pelo usuário **`request.form['username']`** e **`request.form[password']`**.

Vamos agora aplicar estes conceitos ao nosso tutorial.

Primeiro, vamos editar o arquivo de template **`formulario-contato.html`** para nomearmos os campos do formulário, que serão os nomes que utilizaremos como chaves no atributo form. 

Localize os campos input e insira a propriedade name, como nas linhas abaixo:

```
<input type="text" class="form-control" id="form_input_Nome" name="nome">

<input type="text" class="form-control" id="form_input_Telefone" name="telefone">

<input type="text" class="form-control" id="form_input_DataNascimento" name="data_nascimento">

<input type="email" class="form-control" id="form_input_Email" name="email">
```

Agora vamos alterar o arquivo **`app.py`**, para incluir a chamada à biblioteca request e inserir nas rotas **`/adicionar`** e **`/editar`** os comandos para leitura dos dados enviados.

O arquivo **`app.py`** ficará assim:

```
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
```

## 7. Banco de Dados

Chegamos agora à parte em que faremos a integração da nossa aplicação com os dados que estão armazenados no banco de dados. Nossa aplicação fará operações de leitura e escrita no banco de dados.

Vamos utilizar o banco de dados SQLite devido a sua facilidade de configuração e manipulação, sem a necessidade de instalarmos e configurarmos um serviço a parte e pela aplicação ser uma aplicação pequena.

Na seção 2 deste tutorial, apresentamos os passos para a criação do banco de dados, portanto presumimos que o banco de dados já tenha sido criado em sua aplicação.

Para facilitar nosso trabalho e reutilizarmos códigos, evitando a sobrescrita de códigos, vamos criar uma classe que nos auxiliará com métodos para as operações necessárias com banco de dados. Para isto vamos criar um arquivo, na raíz do projeto, chamado **`db.py`**.

Toda vez que uma requisição for recebida e tivermos a necessidade de trabalhar com banco de dados, temos a necessidade de criar um objeto que mantém a conexão com o banco. Ao final das operações, devemos fechar esta conexão. Além disso, também temos operações de consulta e manipulação dos dados retornados, além de operações para inserir ou editar dados. Nossa classe irá abranger estas operações básicas.

Arquivo **`db.py`**:

```
import sqlite3

class DB:
    connection = None

    def connect(self):
        self.connection = sqlite3.connect('db/agenda.db')
        self.connection.row_factory = sqlite3.Row

    def close(self):
        self.connection.close()

    def read(self, sql):
        if self.connection == None:
            self.connect()

        cursor = self.connection.execute(sql)
        return cursor.fetchall()

    def write(self, sql, values):
        if self.connection == None:
            self.connect()

        self.connection.execute(sql, values)
        self.connection.commit()
```

Teremos que realizar algumas alterações no arquivo **`app.py`**, para adicionar algumas novas bibliotecas que iremos utilizar, como: **redirect** (utilizada para redirecionar requisições dentro dos comandos Python), **url_for** (para remontar a URL de uma função), **flash** (grava mensagens entre requisições) e a inclusão da biblioteca de manipulação do banco de dados que criamos anteriormente.

As linhas iniciais do arquivo ficarão assim:

```
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from db import DB

app = Flask(__name__)
app.secret_key = b'\xa0\xdd\x8b\xe05\x00\tP\xb7\x94_\xe9'
```

A entrada **`app.secret_key`** é necessária para utilização das mensagens flash.

Vamos agora alterar as rotas para inserir as ações que envolvem o banco de dados. A primeira que iremos alterar é a rota **`/`** ou **`/listar`**. Nesta rota, temos que realizar uma consulta ao banco de dados para obter o conjunto de registros e exibí-los ao usuário.

```
@app.route("/")
@app.route("/listar")
def listar_contatos():
    conn = DB()
    rows = conn.read("SELECT id, nome, telefone, data_nascimento, email FROM contatos ORDER BY nome")
    conn.close()
    return render_template("listar-contatos.html", rows=rows)
```

No trecho acima a variável **conn** é nosso objeto para manipulação com o banco de dados. Na sequência, adicionamos uma variável chamada **rows** que receberá o conjunto de dados do banco de dados, consultados a partir da string SQL declarada como parâmetro do método **read()**. O resultado obtido após a consulta é passado ao template, através do parâmetro que chamamos de **rows** também.

Feita a alteração no arquivo **`app.py`**, agora temos que alterar o arquivo **`listar-contatos.html`**:

```
    <div class="row py-5">

        {% if get_flashed_messages() %}
        <div class="alert alert-info">
            {% for message in get_flashed_messages() %}
                {{ message }}
            {% endfor %}
        </div>
        {% endif %}

        <table class="table table-hover table-striped ">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Nome</th>
                    <th>Telefone</th>
                    <th>Data de Nascimento</th>
                    <th>E-mail</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>

                {% for row in rows %}
                <tr>
                    <td>{{ row['id'] }}</td>
                    <td>{{ row['nome'] }}</td>
                    <td>{{ row['telefone'] }}</td>
                    <td>{{ row['data_nascimento'] }}</td>
                    <td>{{ row['email'] }}</td>
                    <td>
                        <a href="/visualizar/{{ row['id'] }}" class="text-dark">Visualizar</a> |
                        <a href="/editar/{{ row['id'] }}" class="text-dark">Editar</a> |
                        <a href="/excluir/{{ row['id'] }}" class="text-danger delete-item">Excluir</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
```

Neste arquivo incluímos um trecho de código referente à exibição de mensagens do tipo **flash()**. Utilizaremos isto para exibir mensagens de feedback ao usuário. Também foi alterado o trecho que exibe as linhas de resultado. Criamos um bloco de repetições **`{% for row in rows %}`** e em cada célula alteramos o texto de marcação para o dado do banco de dados a ser exibido, exemplo: **`{{ row['nome'] }}`**.

A próxima rota a ser ajustada é a **/visualizar**. Nesta rota, devemos consultar o banco de dados para recuperar a informação do registro, passado na URL através da variável **id_contato**. Após recuperar o registro este é repassado ao template para exibição dos dados.

```
@app.route("/visualizar/<int:id_contato>")
def visualizar_contato(id_contato):
    conn = DB()
    #Recuperamos os dados do registro a ser editado
    record = conn.read_one(f"SELECT * FROM contatos WHERE id={id_contato}")
    conn.close()

    return render_template("visualizar-contato.html", dados=record)
```

E o arquivo **`visualizar-contato.html`**, alterar as linhas abaixo:

```
        <table class="table table-hover table-striped ">
            <tbody>
                <tr>
                    <th width="200">#</th>
                    <td>{{ dados['id'] }}</td>
                </tr>
                <tr>
                    <th>Nome</th>
                    <td>{{ dados['nome'] }}</td>
                </tr>
                <tr>
                    <th>Telefone</th>
                    <td>{{ dados['telefone'] }}</td>
                </tr>
                <tr>
                    <th>Data de Nascimento</th>
                    <td>{{ dados['data_nascimento'] }}</td>
                </tr>
                <tr>
                    <th>E-mail</th>
                    <td>{{ dados['email'] }}</td>
                </tr>
                <tr>
                    <th>Data de Cadastro</th>
                    <td>{{ dados['data_cadastro'] }}</td>
                </tr>
            </tbody>
        </table>

        <div class="d-flex">
            <a href="/editar/{{ dados['id'] }}" class="btn btn-success">Editar</a>
            <a href="/excluir/{{ dados['id'] }}" class="btn btn-danger ms-2 delete-item">Excluir</a>
            <a href="/listar" class="ms-auto btn btn-dark fw-bold">&lt;- Voltar</a>
        </div>
```

Na sequência, vamos ajustar a rota **/adicionar**. Nesta rota, devemos verificar se recebemos uma requisição do tipo POST, quando o usuário envia o formulário. Neste caso, devemos obter os dados e salvá-los no banco de dados.

```
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

    return render_template("formulario-contato.html", title="Adicionar Contato", form_action="/adicionar", dados=None)
```

Em seguida vamos alterar a rota **/editar**. Aqui temos que recuperar o registro que será editado. O mesmo é repassado ao template através da variável dados. Assim como na rota anterior, verificamos se recebemos uma requisição do tipo POST, e quando recebida, temos que alterar os dados no banco de dados.

```
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
```

No arquivo de template não faremos alterações, pois em seções anteriores já exibimos a versão final. No formulário os detalhes importantes são:
* **{{title}}**: indica o título da página, que se alterna quando a ação é para adicionar um novo contato ou quando estamos editando;
* Propriedade **name=""**: indica o nome da variável para obtenção dos dados
* Propriedades **value=""**: valor exibido quando estamos editando o formulários
* Classes **.phone-mask** e **.date-mask**: indica que o campo conterá uma máscara para digitação dos dados do tipo telefone e data respectivamente. Estas máscaras são adicionadas através de instruções javascript. 

Finalizando, vamos editar a rota **/excluir**. Nesta rota fazemos a exclusão de um registro no banco de dados e posteriormente, redirecionamos o usuário para a listagem de dados exibindo uma mensagem de feedback.

```
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
```

Pronto. Realizadas alterações, podemos realizar os testes das funcionalidades da nossa aplicação, inserindo, editando, visualizando e excluindo dados.
