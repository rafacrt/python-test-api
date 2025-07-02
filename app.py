from flask import Flask, jsonify

app = Flask(__name__)

def normalize(cpf: str) -> str:
    return ''.join(ch for ch in cpf if ch.isdigit())

with open('blacklist.txt') as f:
    blacklisted = { normalize(line) for line in f }

@app.route('/<cpf>')
def check_cpf(cpf):
    ncpf = normalize(cpf)
    status = 'block' if ncpf in blacklisted else 'free'
    return jsonify({'status': status})

app.run(host='0.0.0.0', port=5000)
