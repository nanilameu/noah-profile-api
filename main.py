
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_profile', methods=['POST'])
def get_profile():
    data = request.json
    email = data.get('email')

    # Simulação de resposta fixa (substituir com integração Airtable no Make)
    if email == "elainelameu40@gmail.com":
        profile = {
            "nome_completo": "Elaine Lameu",
            "email": "elainelameu40@gmail.com",
            "cidade_estado": "Campo Grande - MS",
            "registro_profissional": "CAU A237211-8",
            "meta_faturamento_mensal": "R$ 20.000",
            "custos_fixos_variaveis": "R$ 6.000",
            "portfolio": "https://elainelameu.arq.br",
            "nivel_trabalho": "Avançado",
            "experiencia_anos": "10",
            "nichos_atuacao": "Residencial, comercial e corporativo",
            "servicos_oferecidos": "Projetos arquitetônicos, detalhamentos, consultorias",
            "softwares_utilizados": "SketchUp, AutoCAD, Layout, Lumion",
            "estrutura_trabalho": "Sozinha",
            "tem_cnpj": "Sim",
            "interesse_parcerias": "Sim",
            "atende_online": "Sim, para todo o Brasil",
            "sobre_voce": "Sou arquiteta há 10 anos, apaixonada por transformar sonhos em projetos reais.",
            "expectativa_noah": "Quero precificar com mais segurança e fechar mais contratos"
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
