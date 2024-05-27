# Pipeline de ETL para Personalização de Mensagens de Marketing

## 📒 Descrição
Este projeto desenvolve um pipeline de ETL (Extract, Transform, Load) para personalizar mensagens de marketing para clientes de um banco. Os dados dos clientes são extraídos de uma API, transformados usando a API do ChatGPT para gerar mensagens personalizadas, e carregados de volta na API.

## 🤖 Tecnologias Utilizadas
- **Python**: Linguagem de programação principal para o desenvolvimento do pipeline.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **OpenAI API**: Usada para gerar mensagens personalizadas com o ChatGPT.

## 🧐 Processo de Criação
1. **Configuração do Ambiente**:
   - Criação de um ambiente virtual para gerenciar as dependências do projeto.
   - Instalação das bibliotecas necessárias (`requests`, `pandas`, `openai`).

2. **Desenvolvimento do Pipeline ETL**:
   - **Extract**: Leitura dos IDs dos usuários de um arquivo CSV e extração dos dados dos clientes de uma API.
   - **Transform**: Geração de mensagens personalizadas para cada cliente usando a API do ChatGPT.
   - **Load**: Atualização dos dados dos clientes na API com as mensagens geradas.

3. **Execução do Pipeline**:
   - O script `etl_pipeline.py` é executado para processar os dados dos clientes e atualizar a API.

4. **Publicação no GitHub**:
   - Criação de um repositório no GitHub para versionar e compartilhar o projeto.

## 🚀 Resultados
- **Automação do Processo**: O pipeline ETL automatiza a personalização de mensagens de marketing para os clientes, economizando tempo e esforço manual.
- **Mensagens Personalizadas**: Cada cliente recebe uma mensagem única e relevante, aumentando o engajamento e a satisfação do cliente.
- **Integração Eficiente**: A integração com a API do ChatGPT permite a geração de conteúdo de alta qualidade de forma rápida e eficiente.

## 💭 Reflexão (Opcional)
Criar um pipeline ETL que integra a API do ChatGPT foi um desafio interessante. A combinação de extração de dados, transformação usando IA generativa e carregamento dos dados transformados de volta para a API mostrou-se poderosa e eficiente. Este projeto ilustra como as tecnologias de IA podem ser aplicadas para personalizar e melhorar a comunicação com os clientes de forma automatizada e escalável.
