#ETAPA EXTRACT

import pandas as pd
import requests
import json

# URL base da API
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# Função para obter os dados do usuário pelo ID
def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

# Lendo os IDs dos usuários do arquivo CSV
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()

# Obtendo os dados dos usuários
users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

#importar API do OpenAI

#ETAPA TRANSFORMAÇÃO

import openai

# Sua chave de API da OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Função para gerar a mensagem personalizada
def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

# Gerando as mensagens para cada usuário
for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

#ETAPA LOAD

# Função para atualizar os dados do usuário
def update_user(user):
    response = requests.put(f'{sdw2023_api_url}/users/{user["id"]}', json=user)
    if response.status_code == 200:
        print(f"Usuário {user['id']} atualizado com sucesso.")
    else:
        print(f"Falha ao atualizar o usuário {user['id']}.")

# Atualizando os usuários na API
for user in users:
    update_user(user)
