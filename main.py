from flask import Flask, render_template, redirect, request

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

    return redirect("/cadastro")

if __name__ == "__main__":
    app.run(debug=True)