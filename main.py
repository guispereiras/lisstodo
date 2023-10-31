from flask import Flask, render_template, redirect, request

app = Flask(__name__)



@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/cadastro")
def atributos():
     return render_template("cadastro.html")

@app.route("/login", methods=['POST'])
def login():
    
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    print(nome)
    print(senha)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)