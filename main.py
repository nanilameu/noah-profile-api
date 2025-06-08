from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_profile', methods=['POST'])
def get_profile():
    data = request.json
    email = data.get('email')

    # Simulação de resposta (no futuro, você vai buscar via Make/Airtable)
    if email == "elainelameu40@gmail.com":
        profile = {
            "name": "Elaine Lameu",
            "especialidade": "Arquitetura e Urbanismo",
            "cidade_regiao": "Campo Grande - MS",
            "meta_faturamento_mensal": "R$ 20.000",
            "modelo_precificacao": "por hora",
            "tom_linguagem": "técnico",
            "tipo_cliente_comum": "B2B",
        }
    else:
        profile = None

    if profile:
        return jsonify({
            "success": True,
            "profile": profile
        })
    else:
        return jsonify({
            "success": False,
            "message": "Perfil não encontrado para este e-mail."
        }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
