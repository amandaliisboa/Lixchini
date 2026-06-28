import sqlite3

class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        # conecta ao banco de dados (cria o arquivo se nao existir)
        self.connection = sqlite3.connect(db_name)
        # cria a tabela de scores se ainda nao existir
        self.connection.execute('''
                                CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                score INTEGER NOT NULL,
                                date TEXT NOT NULL)
                            '''
                                )

    def save(self, score_dict: dict):
        # insere um novo registro de score no banco
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        # busca os 10 maiores scores em ordem decrescente
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        # fecha a conexão com o banco
        return self.connection.close()