from lisstodo.ext.connection import mydb 



def create(email, nome, idade, sexo, senha):
    cursor = mydb.cursor()
    comando = f'SELECT email FROM usuarios where email = "{email}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    if resultado:
        email_banco = resultado[0]
        if email == email_banco:
            print("E-mail já cadastrado")
            return("E-mail já cadastrado")
        else:
            comando = f'INSERT INTO usuarios (ID, NOME, EMAIL, SEXO, IDADE, SENHA) VALUES (DEFAULT, "{nome}", "{email}", "{sexo}", "{idade}","{senha}")'
            cursor.execute(comando)
            mydb.commit()
            print('Registro adicionado com sucesso')
            cursor.close()
            mydb.close()

def login(email, senha):
    cursor = mydb.cursor()

    comando = f'SELECT senha FROM usuarios WHERE email = "{email}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    if resultado:
        senha_banco = resultado[0]
        if senha == senha_banco:
            return("Login bem-sucedido")
        else:
            return("Senha incorreta")
    else:
        return("Email não encontrado")
