from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

modelos = [
"🚀 {profissao} | apaixonado por {habilidade} | 📍{cidade}",
"🔥 {profissao} ajudando pessoas com {habilidade}",
"💡 Dicas de {habilidade} todos os dias | {profissao}",
"✨ {profissao} | vivendo em {cidade}",
"📈 Transformando {habilidade} em resultados"
]

@app.route("/", methods=["GET","POST"])
def home():

    bios = []

    if request.method == "POST":

        profissao = request.form["profissao"]
        habilidade = request.form["habilidade"]
        cidade = request.form["cidade"]

        for i in range(5):
            modelo = random.choice(modelos)

            bio = modelo.format(
                profissao=profissao,
                habilidade=habilidade,
                cidade=cidade
            )

            bios.append(bio)

    return render_template("index.html", bios=bios)


port = int(os.environ.get("PORT", 10000))

app.run(host="0.0.0.0", port=port)