# Encurtador de Links
Este projeto é um encurtador de URLs baseado no Django. Ele permite que os usuários encurtem URLs longas em URLs curtas que podem ser facilmente compartilhadas em redes sociais, por exemplo.
Ele foi feito com base no vídeo do Caio Sampaio do canal [pythonando](https://www.youtube.com/@pythonando/).

# Instalação
Para instalar o projeto, siga estes passos:

1. Clone o repositório usando o comando abaixo:
```bash
git clone https://github.com/SeverinoRibNeto/encurtador-link.git
```
2. Crie um ambiente virtual usando o comando:
#### No Windows
```bash
python -m venv venv
```
#### No Linux
```bash
python3 -m venv venv
```

3. Ative o ambiente virtual usando o comando:
#### No Windows
```bash
.\venv\Scripts\activate
```
#### No Linux
```bash
source myenv/bin/activate
```
4. Instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```
5. Execute as migrações usando o comando:
```bash
python manage.py migrate
```

# Uso
Para usar o encurtador de links, siga estes passos:
1. Execute o servidor usando o comando:
```bash
python manage.py runserver
```
2. Acesse o site em seu navegador usando o endereço http://localhost:8000.
3. Digite a URL que deseja encurtar na caixa de texto "Link para encurtar" e a o atalho no "Link encurtado" e clique em "Encurtar".
4. Copie a URL encurtada e compartilhe onde quiser.

# Licença
Este projeto está licenciado sob a licença MIT.
