from flask import Flask, render_template

app = Flask(__name__)

# ==========================
# Configurações
# ==========================

app.config["SECRET_KEY"] = "lakevision"

# ==========================
# Rotas
# ==========================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cabine")
def cabine():
    return render_template("cabine.html")


# (futuramente)
@app.route("/analise")
def analise():
    return render_template("analise.html")
# ==========================
# Inicialização
# ==========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )