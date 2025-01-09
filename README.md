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

## 2. Organizando a aplicação

Manter uma boa estrutura e organização dos arquivos torna o projeto mais legível e de fácil manutenção. Desta forma apresentamos uma estrutura de arquivos e diretórios que utilizaremos neste tutorial.

```
|-- ifsp-flask-tutorial
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
```

* O diretório **ifsp-flask-tutorial** é o diretório de nossa aplicação.
* O diretório **static** reúne os arquivos estáticos da aplicação que serão referenciados pelos códigos HTML. Dentro deste diretório, foram criados outros três diretórios, sendo eles:
    * **css:** para armazenar os arquivos de estilos utilizados pela aplicação
    * **images:** para armazenar as imagens
    * **js:** para armazenar os scripts em linguagem javascript, responsáveis pelo controle da interação e elementos HTML.
* O diretório **templates** irá abrigar os arquivos contendo códigos HTML que serão utilizados pela aplicação para a renderização dos conteúdos.
* O arquivo **`app.py`** contém os códigos já descritos na seção anterior.

## 3. Rotas

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

## 4. Templates

Todas as rotas são associadas a uma função que retorna o conteúdo do processamento. Retornar todo o código HTML dentro de uma função aumenta consideravelmente as linhas de código e dificulta a manutenção de um arquivo.

Uma boa prática é a utilização de templates.
Templates são arquivos estáticos que podem conter espaços (placeholders) para dados dinâmicos. Um arquivo de template é renderizado (processado) com dados específicos para produzir o documento final.

Estes arquivos, por padrão, são armazenados no diretório **templates/** de sua aplicação. Para melhorar a organização, dependendo do tamanho de sua aplicação, os arquivos também podem ser organizados em subdiretórios.

Os arquivos de template são arquivos HTML que podem conter espaços (placeholders) delimitados por:
* {{ }} - expressões que produzem saídas no documento, funcionando como um print do Python.
* {% %} - expressões de controle de fluxo ou funções (como if, for, etc).

Para utilizarmos templates devemos adicionar a biblioteca **render_template**, que adiciona a função de mesmo nome que retorna o resultado do processamento do arquivo de template como um arquivo estático.

Vejamos um exemplo de uso:

```
from flask import render_template
@app.route(“/exemplo-template”)
def exemplo_template():
    return render_template(“exemplo.html”)
```

**Passando valores dinâmicos para um template**

```
from flask import render_template
@app.route(“/exemplo-template-2”)
def exemplo_template2():
    return render_template(“exemplo2.html”, teste=”Este é um valor que foi repassado ao template”)
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
