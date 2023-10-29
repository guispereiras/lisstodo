from mysql.connector import errorcode
import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='eanl4i1omny740jw.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        user='bh0njlgv0va2irjp',
        password='c7p5923wdin55i2q',
        database='kg21sgihlerygjmb', 
    )
    print('Conectado')
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Algo errado com o usuario ou senha.')
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe')
    else:
        print(e)
        