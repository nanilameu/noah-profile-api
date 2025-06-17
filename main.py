from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulação de banco de dados (você pode integrar com o Airtable depois)
PERFIS = {
    "elainelameu40@gmail.com": {
        "nome_completo": "Elaine Lameu",
        "experiencia_anos": "10",
        "nichos_atuacao": "Residencial, comercial e corporativo",
        "estrutura_trabalho": "Precificar com mais segurança e fechar mais contratos",
        "tem_cnpj": "Sim"
    }
}

@app.route('/get_profile', methods=['POST'])
def get_profile():
    try:
        data = request.get_json()
        email = data.get('email')

        if not email:
            return jsonify({"success": False, "error": "Email não fornecido"}), 400

        profile = PERFIS.get(email)

        if not profile:
            return jsonify({"success": False, "error": "Perfil não encontrado"}), 404

        return jsonify({"success": True, "profile": profile})

    except Exception as e:
        print(f"Erro em /get_profile: {e}")
        return jsonify({"success": False, "error": "Erro interno"}), 500


@app.route('/ask_noah', methods=['POST'])
def ask_noah():
    try:
        data = request.get_json()
        email = data.get('email')
        question = data.get('question')

        if not email or not question:
            return jsonify({"success": False, "error": "Email ou pergunta ausentes"}), 400

        profile = PERFIS.get(email)

        if not profile:
            return jsonify({"success": False, "error": "Perfil não encontrado"}), 404

        # Resposta básica de exemplo
        if "orçamento" in question.lower():
            resposta = f"Olá {profile['nome_completo']}, vou te ajudar a montar o orçamento! Qual o tamanho do projeto?"
        else:
            resposta = f"{profile['nome_completo']}, recebi sua pergunta: '{question}', mas preciso de mais detalhes para te ajudar melhor."

        return jsonify({"success": True, "reply": resposta})

    except Exception as e:
        print(f"Erro em /ask_noah: {e}")
        return jsonify({"success": False, "error": "Erro interno"}), 500


if __name__ == '__main__':
    app.run(debug=True)
