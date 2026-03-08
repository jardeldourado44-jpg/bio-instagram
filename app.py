from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

emojis = ["🚀","🔥","💡","✨","📈","🌍","⚡","🎯","📚","💼","🎥","🎧","💻","🧠","🛠"]

modelos = [
"{emoji} {profissao} apaixonado por {habilidade}",
"{emoji} ajudando pessoas com {habilidade}",
"{emoji} vivendo em {cidade} e trabalhando como {profissao}",
"{emoji} transformando {habilidade} em resultados",
"{emoji} criador focado em {habilidade}",
"{emoji} compartilhando conhecimento sobre {habilidade}",
"{emoji} construindo algo grande em {cidade}",
"{emoji} especialista em {habilidade}",
"{emoji} aprendendo e ensinando {habilidade}",
"{emoji} criando impacto com {habilidade}",
]

# cria automaticamente 50 estilos
while len(modelos) < 50:
    modelos.append(random.choice(modelos))

def gerar_bios(profissao, habilidade, cidade):

    bios = []

    for i in range(10):

        modelo = random.choice(modelos)

        bio = modelo.format(
            emoji=random.choice(emojis),
            profissao=profissao,
            habilidade=habilidade,
            cidade=cidade
        )

        bios.append(bio)

    return bios

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gerar", methods=["POST"])
def gerar():

    data = request.json

    profissao = data["profissao"]
    habilidade = data["habilidade"]
    cidade = data["cidade"]

    bios = gerar_bios(profissao, habilidade, cidade)

    return jsonify(bios)

if __name__ == "__main__":
    app.run()