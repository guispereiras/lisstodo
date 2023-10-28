from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira pagina 
# route _> listech.com/usuarios
# função -> o que quero exibir naquela pagina


@app.route("/")
# decorator -> linha de código para atribuir uma nova funcionalidade para a função abaixoss
def homepage():
    return render_template("homepage.html")


@app.route("/cadastro")
def atributos():
    return render_template("cadastro.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

