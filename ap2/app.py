from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        resultado = numero + 2
        return f'O número enviado foi {numero} e o resultado é {resultado}.'

if __name__ == '__main__':
    app.run(debug=True)
