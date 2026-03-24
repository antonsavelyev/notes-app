from flask import Flask

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return '<br>'.join(notes) or 'Заметок пока нет'

@app.route('/add/<note>')
def add(note):
    notes.append(note)
    return f'Добавлено: {note}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
