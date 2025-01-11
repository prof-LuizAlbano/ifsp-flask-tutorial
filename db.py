import sqlite3

class DB:
    connection = None

    '''
    Este método tem como objetivo estabelecer uma conexão com o arquivo de dados SQLite
    e configurar o formato de retorno dos dados em consultas ao banco. 
    '''
    def connect(self):
        self.connection = sqlite3.connect('db/agenda.db')
        self.connection.row_factory = sqlite3.Row


    '''
    Fecha a conexão com o banco de dados
    '''
    def close(self):
        self.connection.close()


    '''
    Método utilizado para realizar consultas ao banco de dados.
    Recebe como parâmetro a string de consulta ao banco e retorna
    o conjunto de resultados encontrado.
    '''
    def read(self, sql):
        if self.connection == None:
            self.connect()

        cursor = self.connection.execute(sql)
        return cursor.fetchall()
    

    '''
    Método utilizado para realizar consultas ao banco de dados.
    Recebe como parâmetro a string de consulta ao banco e retorna
    o conjunto de dados de uma única linha.
    '''
    def read_one(self, sql):
        if self.connection == None:
            self.connect()

        cursor = self.connection.execute(sql)
        return cursor.fetchone()


    '''
    Método utilizado para realizar ações que modifiquem os dados  no banco de dados.
    Recebe como parâmetro a string de manipulação (INSERT, UPDATE ou DELETE) e
    os valores a serem substituídos nas lacunas das string, em formato de tupla.
    '''
    def write(self, sql, values):
        if self.connection == None:
            self.connect()

        self.connection.execute(sql, values)
        self.connection.commit()