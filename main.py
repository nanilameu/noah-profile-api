from flask import Flask, request, jsonify
import requests
import os

# Configurações do Airtable
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY') or 'YOUR_API_KEY'
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID') or 'YOUR_BASE_ID'
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME') or 'YOUR_TABLE_NAME'

AIRTABLE_URL = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# Inicializa o Flask
app = Flask(__name__)

@app.route('/get_profile', methods=['POST'])
def get_profile():
    try:
        data = request.get_json()

        if not data or 'email' not in data:
            return jsonify({'success': False, 'error': 'Missing email parameter'}), 400

        email_to_search = data['email'].strip().lower()

        headers = {
            'Authorization': f'Bearer {AIRTABLE_API_KEY}',
            'Content-Type': 'application/json'
        }

        params = {
            'filterByFormula': f"LOWER({{Email}}) = '{email_to_search}'",
            'maxRecords': 1
        }

        response = requests.get(AIRTABLE_URL, headers=headers, params=params)

        if response.status_code != 200:
            return jsonify({'success': False, 'error': 'Airtable request failed', 'status_code': response.status_code}), 500

        records = response.json().get('records', [])

        if not records:
            return jsonify({'success': False, 'error': 'Profile not found'}), 404

        record = records[0]['fields']

        # Monte a resposta com os campos que você deseja retornar
        profile = {
            'email': record.get('Email', ''),
            'estrutura_trabalho': record.get('Estrutura de trabalho', ''),
            'expectativa_noah': record.get('Expectativa com a Noah', ''),
            'experiencia_anos': record.get('Experiência em anos', ''),
            'interesse_parcerias': record.get('Tem interesse em parcerias?', ''),
            'meta_faturamento_mensal': record.get('Meta de faturamento mensal', ''),
            'nichos_atuacao': record.get('Nichos de atuação', ''),
            'nivel_trabalho': record.get('Nível de trabalho', ''),
            'nome_completo': record.get('Nome completo', ''),
            'portfolio': record.get('Portfólio', ''),
            'registro_profissional': record.get('Registro profissional', ''),
            'servicos_oferecidos': record.get('Serviços oferecidos', ''),
            'sobre_voce': record.get('Sobre você', ''),
            'softwares_utilizados': record.get('Softwares que utiliza', ''),
            'tem_cnpj': record.get('Possui CNPJ?', '')
        }

        return jsonify({'success': True, **profile}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Roda a aplicação Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
