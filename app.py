from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random
import csv
from pathlib import Path

app = Flask(__name__)

emojis = ["🚀", "🔥", "💡", "✨", "📈", "🌍", "⚡", "🎯", "📚", "💼", "🎥", "🎧", "💻", "🧠", "🛠"]

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

# completa automaticamente até 50 modelos
while len(modelos) < 50:
    modelos.append(random.choice(modelos))


def gerar_bios(profissao, habilidade, cidade):
    bios = []
    for _ in range(10):
        modelo = random.choice(modelos)
        bio = modelo.format(
            emoji=random.choice(emojis),
            profissao=profissao,
            habilidade=habilidade,
            cidade=cidade,
        )
        bios.append(bio)
    return bios


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/gerar", methods=["POST"])
def gerar():
    data = request.get_json(silent=True) or {}

    profissao = data.get("profissao", "").strip()
    habilidade = data.get("habilidade", "").strip()
    cidade = data.get("cidade", "").strip()

    if not profissao or not habilidade or not cidade:
        return jsonify({"erro": "Preencha profissão, habilidade e cidade."}), 400

    bios = gerar_bios(profissao, habilidade, cidade)
    return jsonify({"bios": bios})


@app.route("/capturar-lead", methods=["POST"])
def capturar_lead():
    data = request.get_json(silent=True) or {}

    nome = data.get("nome", "").strip()
    email = data.get("email", "").strip()

    if not nome or "@" not in email:
        return jsonify({"erro": "Informe nome e e-mail válido."}), 400

    base_dir = Path(__file__).parent
    leads_dir = base_dir / "data"
    leads_dir.mkdir(exist_ok=True)
    leads_file = leads_dir / "leads.csv"

    novo_arquivo = not leads_file.exists()
    with leads_file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if novo_arquivo:
            writer.writerow(["nome", "email", "origem", "data_hora"])
        writer.writerow([nome, email, "landing_page", datetime.now().isoformat()])

    return jsonify({"mensagem": "Lead salvo com sucesso!"})


if __name__ == "__main__":
    app.run()
