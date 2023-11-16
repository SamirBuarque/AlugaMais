import psycopg2

# criando a conexão com o db
connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
print('Conectado ao banco de dados')

# comandos tem efeito imediato. Caso fosse False, seria preciso dar commit após cada comando sql
connection.autocommit = True

#criando o cursor
cursor = connection.cursor()

cursor.execute("CREATE DATABASE clients")
print('Banco de dados criado com sucesso')

connection.close()
print('Encerrando conexao com o banco de dados')