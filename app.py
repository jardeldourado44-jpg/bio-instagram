from flask import Flask, render_template, request
import random

app = Flask(__name__)

modelos = [
"🚀 {profissao} | apaixonado por {habilidade} | 📍{cidade}",
"🔥 {profissao} ajudando pessoas com {habilidade}",
"💡 Dicas de {habilidade} todos os dias",
"✨ {profissao} vivendo em {cidade}",
"📈 Transformando {habilidade} em resultados",
"🌍 {profissao} compartilhando conhecimento",
"⚡ Especialista em {habilidade}",
"🎯 {profissao} focado em crescimento",
"📚 Aprendendo e ensinando {habilidade}",
"🚀 Construindo algo grande em {cidade}"
]

@app.route("/", methods=["GET", "POST"])
def home():

    bios = []

    if request.method == "POST":

        profissao = request.form["profissao"]
        habilidade = request.form["habilidade"]
        cidade = request.form["cidade"]

        for i in range(10):

            modelo = random.choice(modelos)

            bio = modelo.format(
                profissao=profissao,
                habilidade=habilidade,
                cidade=cidade
            )

            bios.append(bio)

    return render_template("index.html", bios=bios)


if __name__ == "__main__":
    app.run()