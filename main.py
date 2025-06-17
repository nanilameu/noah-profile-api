from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Rota raiz para teste
@app.route('/')
def index():
    return "Noah Profile API is running."

# Endpoint /get_profile
@app.route('/get_profile', methods=['POST'])
def get_profile():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"success": False, "error": "Missing JSON in request"}), 400

        email = data.get('email')
        if not email:
            return jsonify({"success": False, "error": "Missing 'email' field in request"}), 400

        if email == "elainelameu40@gmail.com":
            profile = {
                "email": email,
                "estrutura_trabalho": "Sozinha",
                "expectativa_noah": "Quero precificar com mais segurança e fechar mais contratos",
                "experiencia_anos": "10",
                "interesse_parcerias": "Sim",
                "meta_faturamento_mensal": "R$ 28.000",
                "nichos_atuacao": "Residencial, comercial e corporativo",
                "nivel_trabalho": "Avançado",
                "nome_completo": "Elaine Lameu",
                "portfolio": "https://elainelameu.arq.br",
                "registro_profissional": "CAU A2937211-0",
                "servicos_oferecidos": "Projetos arquitetônicos, detalhamentos, consultorias",
                "sobre_voce": "Sou arquiteta há 10 anos, apaixonada por transformar sonhos em projetos reais.",
                "softwares_utilizados": "SketchUp, AutoCAD, Layout, Lumion",
                "tem_cnpj": "Sim"
            }

            return jsonify({"success": True, "profile": profile}), 200
        else:
            return jsonify({"success": False, "error": "Profile not found for this email."}), 404

    except Exception as e:
        print(f"Error in /get_profile: {e}")
        return jsonify({"success": False, "error": "Internal server error"}), 500

# Endpoint /ask_noah
@app.route('/ask_noah', methods=['POST'])
def ask_noah():
    try:
        data = request.get_json()
        email = data.get('email')
        question = data.get('question')

        if not email or not question:
            return jsonify({"success": False, "error": "Missing email or question"}), 400

        if email == "elainelameu40@gmail.com":
            profile = {
                "nome_completo": "Elaine Lameu",
                "experiencia_anos": "10"
                # Pode expandir com mais campos se quiser
            }
        else:
            return jsonify({"success": False, "error": "Profile not found for this email."}), 404

        # Resposta simulada com base na pergunta
        if "orçamento" in question.lower():
            resposta = f"Olá {profile['nome_completo']}, vou te ajudar a montar o orçamento! Qual o tamanho do projeto?"
        else:
            resposta = f"{profile['nome_completo']}, recebi sua pergunta: '{question}', mas preciso de mais detalhes para ajudar."

        return jsonify({"success": True, "reply": resposta})

    except Exception as e:
        print(f"Error in /ask_noah: {e}")
        return jsonify({"success": False, "error": "Internal server error"}), 500

# Execução compatível com Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
