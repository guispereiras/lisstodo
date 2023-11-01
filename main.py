from flask import Flask, render_template, redirect, request
from connection import create, loginsexo


app = Flask(__name__)
# Rota home
@app.route("/") 
def homepage():
    return render_template("home.html")

# Rota para ler o login.html antes de executa-lo (Gambiarrazap)
@app.route("/login")
def login1():

    return render_template("login.html")

# Rota cadastro
@app.route("/cadastro")
def atributos():
     return render_template("cadastro.html")

# Rota ler login.html e puxar os dados dos input's
@app.route("/login", methods=['POST'])
def login2():
    
    email = request.form.get("email")
    senha = request.form.get("senha")
    print(email)
    print(senha)

    loginsexo(email, senha)

    return redirect("/")

# Rota ler cadastro.html e puxar os dados dos input's
@app.route('/cadastro', methods=['POST'])
def cadastro():

    email = request.form.get("email")
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    sexo1 = request.form.get("sexo1")
    sexo2 = request.form.get("sexo2")
    senha = request.form.get("senha")

    print(email)
    print(nome)
    print(idade)
    print(sexo1)
    print(sexo2)
    print(senha)

    
    create(email, nome, idade, sexo1, senha)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)