# Tutorial Flask - Programação Web
Tutorial sobre o uso do framework Flask / Python elaborado para a disciplina de Programação Web, do curso Técnico Integrado em Redes de Computadores do IFSP Campus Pirituba.


**Autores:** Luiz Roberto Albano Junior e Renato Cristiano Montanher.

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
pip install virtualenv
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