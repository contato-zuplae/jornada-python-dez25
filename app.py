from flask import Flask
from flask import render_template

app = Flask(__name__)

cursos = ["Python", "CSharp", "JavaScript"]

@app.get("/")
def home():
    return render_template("index.html", nome="Zuplae")

@app.get("/sobre")
def sobre():
    return "Página sobre"

@app.get("/cursos/<int:id>")
def item(id):
    return f"Item escolhido: {id} = {cursos[id]}"

@app.get("/cursos")
def lista():
    return render_template("cursos.html", itens=cursos)

app.run(debug=True)