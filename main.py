from flask import Flask, render_template, url_for
from modules.calendario import ObterCalendario

app = Flask(__name__)
app.secret_key = 'calendario'

@app.route("/")
def calendario():
    calendario = ObterCalendario()
    matriz_dias = calendario.matriz_dias
    mes_nome = calendario.mes_nome
    dia_hoje = calendario.dia_de_hoje
    mes_numero = calendario.mes_atual
    ano_numero = calendario.ano_numero
    return render_template('index.html',
                           calendario = matriz_dias,
                           mes_nome_atual = mes_nome,
                           dia_hoje = dia_hoje,
                           mes_numero = mes_numero,
                           ano_numero = ano_numero
                           )

if __name__ == '__main__':
    app.run(debug=True)