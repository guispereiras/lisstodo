from flask import Flask, render_template, redirect, request
from lisstodo.blueprints import crud


def init_app(app):
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
    @app.route("/login", methods=['POST', 'GET'])
    def login2():
        
        email = request.form.get("email")
        senha = request.form.get("senha")
        print(email)
        print(senha)

        mensagem = None

        resultado_login = crud.login(email, senha)
        
        if resultado_login == 'Senha incorreta':
            mensagem = 'Senha incorreta. Tente novamente.'
        elif resultado_login == 'Email não encontrado':
            mensagem = 'E-mail não encontrado'
        else:
            return redirect("/")
        
        return render_template("login.html", mensagem=mensagem)

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

        
        crud.create(email, nome, idade, sexo1, senha)

        return redirect("/") 