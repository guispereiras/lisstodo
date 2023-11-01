from mysql.connector import errorcode
import mysql.connector


try:
    conex = mysql.connector.connect(
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


def create(email, nome, idade, sexo, senha):
    cursor = conex.cursor()

    comando = f'INSERT INTO usuarios (ID, NOME, EMAIL, SEXO, IDADE, SENHA) VALUES (DEFAULT, "{nome}", "{email}", "{sexo}", "{idade}","{senha}")'
    cursor.execute(comando)
    conex.commit()
    print('Registro adicionado com sucesso')
    cursor.close()
    conex.close()

def loginsexo(email, senha):
    cursor = conex.cursor()

    comando = f'SELECT senha FROM usuarios WHERE email = "{email}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    if resultado:
        senha_banco = resultado[0]
        if senha == senha_banco:
            print("Login bem-sucedido")
        else:
            print("Senha incorreta")
    else:
        print("Email não encontrado")
