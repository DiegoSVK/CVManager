# Sistema de Recrutamento

## Sobre o Projeto
Projeto que desenvolvi para gerenciar currículos. A ideia é simples: o usuário irá se autenticar para utilizar as funções da plataforma, como inserir e visualizar suas informações.

## Tecnologias Usadas
- **Python**
- **Django**
- **HTML-CSS**
- **Bootstrap**
- **django-crispy-forms**
- **django-formtools**

## Como Instalar
Para configurar o projeto no seu computador, siga estes passos:

1. Clone o repositório: `git clone https://github.com/DiegoSVK/CVManager.git`

2. Instale as dependências: `pip install -r requirements.txt`

## Como Usar
Para executar o servidor Django, siga estas etapas:

1. **Execute as migrações:**
   - No terminal, digite:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

2. **Crie um superusuário:**
   - No terminal, digite:
     ```
     python manage.py createsuperuser
     ```

3. **Inicie o servidor:**
   - No terminal, digite:
     ```
     python manage.py runserver
     ```

