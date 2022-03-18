# fiap-hmv-lambda-custom-message
[![Generic badge](https://img.shields.io/badge/Linguagem-Python-yellow.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/pt/lambda/)

Projeto com os templates de e-mails para o Cognito enviar aos usuários.

Os e-mails são disparados automaticamente pelo Cognito aos usuários quando:

* **Cadastro de usuário (signup)**
    * Ao cadastrar um novo usuário é enviado ao e-mail informado um código de confirmação.

* **Solicitação de novo código de confirmação (resendCode)**
    * Se o usuário não recebeu o e-mail ao se cadastrar, ele pode solicitar um novo reenvio de código para prosseguir com o cadastro.

* **Esqueceu senha (forgotPassword)**
    * Ao esquecer a senha, é enviado um código ao e-mail do usuário para alterar a senha.

Para instalar as dependências:
> pip install -r requirements.txt

### :exclamation: Atualizar o código no lambda
Execute o comando abaixo para gerar o **hmv-signup.zip** e depois faça o upload no lambda pelo console da AWS
> zip -r hmv-custom-message.zip * -x ".git*" -x "README.md" -x coverage.xml -x "venv/*" -x ./package -x "tests/*" -x "test/*" -x Dockerfile -x docker-compose.yml -x ./examples -x functions.json 