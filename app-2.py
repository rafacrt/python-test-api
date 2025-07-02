from flask import Flask, Response

app = Flask(__name__)

def normalize(cpf: str) -> str:
    return ''.join(ch for ch in cpf if ch.isdigit())

with open('blacklist.txt', encoding='utf-8') as f:
    blacklisted = { normalize(line) for line in f }

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Verificador de CPF</title>
      </head>
      <body>
        <h1>Verificador de CPF</h1>
        <form id="cpfForm">
          <input type="text" id="cpf" placeholder="Digite o CPF" />
          <button type="submit">Verificar</button>
        </form>
        <p id="result"></p>
        <script>
          document
            .getElementById('cpfForm')
            .addEventListener('submit', async function(e) {
              e.preventDefault();
              const cpf = document.getElementById('cpf').value;
              const resp = await fetch(`/${cpf}`);
              const text = await resp.text();
              document.getElementById('result').textContent = text;
            });
        </script>
      </body>
    </html>
    '''

@app.route('/<cpf>')
def check_cpf(cpf):
    ncpf = normalize(cpf)
    resultado = 'BLOQUEADO' if ncpf in blacklisted else 'LIVRE'
    return Response(resultado)

app.run(host='0.0.0.0', port=5000)
