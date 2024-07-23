# Consumidor da API do Twitter com FastAPI

Este projeto demonstra como usar o FastAPI para interagir com a API do Twitter. Inclui endpoints para recuperar uma lista de tweets de um usuário especificado.

## Funcionalidades

- Recuperar tweets de um usuário do Twitter especificado.
- Número de tweets a serem recuperados é configurável.
- Documentação disponível através da interface Swagger UI gerada automaticamente pelo FastAPI.

## Requisitos

- Python 3.7+
- Tweepy
- FastAPI
- Uvicorn
- python-dotenv

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/seuusuario/seu-repositorio.git
   cd seu-repositorio
python -m venv venv
Crie e ative um ambiente virtual:

sh
 
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale os pacotes necessários:

sh
 
pip install -r requirements.txt
Crie um arquivo .env no diretório raiz com o seguinte conteúdo:

env
 
TWITTER_API_KEY=sua_chave_api
TWITTER_API_SECRET_KEY=sua_chave_secreta_api
TWITTER_ACCESS_TOKEN=seu_token_de_acesso
TWITTER_ACCESS_TOKEN_SECRET=seu_token_secreto_de_acesso
Substitua os valores de placeholder pelas suas credenciais reais da API do Twitter.

Uso
Inicie a aplicação FastAPI:

sh
uvicorn main:app --reload
Isso iniciará o servidor de desenvolvimento em http://127.0.0.1:8000.

Acesse a documentação da API em:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Para recuperar tweets, faça uma requisição POST para o endpoint /tweets com o seguinte payload JSON:

json
 
{
  "username": "twitter",
  "tweet_count": 5
}
Substitua "twitter" pelo handle do Twitter do usuário e 5 pelo número de tweets que deseja recuperar.

Exemplo
Aqui está um exemplo de como usar a API com curl:

sh
 
curl -X POST "http://127.0.0.1:8000/tweets" -H "Content-Type: application/json" -d '{"username": "twitter", "tweet_count": 5}'
Contribuindo
Se você deseja contribuir para este projeto, siga estes passos:

Faça um fork do repositório.
Crie uma branch para a feature (git checkout -b feature/sua-feature).
Faça commit das suas alterações (git commit -am 'Adicionar nova feature').
Faça push para a branch (git push origin feature/sua-feature).
Crie uma nova Pull Request.
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Agradecimentos
Tweepy por interagir com a API do Twitter.
FastAPI por construir a API.
Uvicorn por servir a aplicação FastAPI.
python-dotenv por carregar variáveis de ambiente.
markdown

### Explicação das Seções

- **Título e Descrição do Projeto:** Descreve brevemente o projeto e suas funcionalidades.
- **Funcionalidades:** Lista as funcionalidades do projeto.
- **Requisitos:** Lista das dependências necessárias para rodar o projeto.
- **Instalação:** Passos para instalar e configurar o projeto.
- **Uso:** Instruções sobre como iniciar o servidor e usar a API.
- **Exemplo:** Exemplo de uso da API.
- **Contribuindo:** Diretrizes para quem deseja contribuir com o projeto.
- **Licença:** Informações sobre a licença do projeto.
- **Agradecimentos:** Reconhecimentos a ferramentas e bibliotecas utilizadas.

Certifique-se de ajustar os detalhes conforme necessário para refletir com precisão seu projeto e suas configurações. Se precisar de mais alguma coisa, é só avisar!
