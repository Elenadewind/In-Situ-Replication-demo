python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    file = request.files['template']
    # Здесь — логика адаптации (из Варианта 2)
    result = "План сборки: использовать Fe вместо Cu (аналог найден)"
    return result

if __name__ == '__main__':
    app.run(debug=True)
