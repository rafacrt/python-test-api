# Verificador de CPF Blacklist

Este repositório contém duas implementações em Python utilizando Flask para atender ao teste de vaga:

* **app.py**
  Faz **exatamente** o que o teste pedia: disponibiliza um endpoint REST em que você passa o CPF pela URL e obtém como resposta apenas `LIVRE` ou `BLOQUEADO` conforme a presença na lista negra. Nem mais, nem menos.

* **app-2.py**
  Versão aprimorada: além da funcionalidade básica, inclui uma página HTML com um campo de input para digitar o CPF e um script JavaScript que consulta a API em background (fetch), exibindo o resultado sem recarregar a página.

---

## Estrutura do projeto

```
python-test-api/
│
├─ app.py         # API básica conforme o teste
├─ app-2.py       # API + interface HTML para verificação dinâmica
├─ blacklist.txt  # Lista de CPFs (um por linha) – pode ter pontos e traço
├─ requirements.txt
└─ README.md
```

## Pré-requisitos

* Python 3.6+
* Flask (instalado via `pip install -r requirements.txt`)

## Como instalar e executar

1. **Clone** este repositório e entre na pasta:

   ```bash
   git clone https://github.com/seu-usuario/python-test-api.git
   cd python-test-api
   ```
2. **(Opcional)** Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   .\venv\Scripts\Activate   # Windows PowerShell
   ```
3. **Instale** as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### app.py (API básica)

1. Certifique-se de que o `blacklist.txt` contenha os CPFs a bloquear (um por linha).
2. Execute:

   ```bash
   python app.py
   ```
3. Acesse ou consulte via `curl`:

   ```bash
   curl http://127.0.0.1:5000/00000000000
   ```

   * Retorna `LIVRE` ou `BLOQUEADO`.

### app-2.py (API + Interface)

1. Mantenha o `blacklist.txt` atualizado.
2. Execute:

   ```bash
   python app-2.py
   ```
3. Abra no navegador:

   ```
   http://127.0.0.1:5000/
   ```
4. Digite o CPF no campo e pressione “Verificar” para ver `LIVRE` ou `BLOQUEADO` sem recarregar.

## Observações

* O servidor do Flask usado aqui é para desenvolvimento/teste. Em produção, use WSGI apropriado (Gunicorn, uWSGI) atrás de um web server.
* Não há funcionalidades extras além das requeridas: cada script cumpre seu propósito específico.

---

**Boa sorte no processo seletivo!**
