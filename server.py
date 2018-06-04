from flask import Flask, render_template

app = Flask(__name__)

emotions_names = ['kind', 'funny', 'depressing', 'action', 'teen',
                 'clever', 'inspiring', 'romantic', 'tense',
                  'atmospheric', 'rude', 'violent', 'scary',
                  'strange', 'touching', 'futuristic', 'unreal',
                  'beautiful', 'gruesome', 'realistic', 'sexy']

emotions_names_ru = ['Добрый', 'Смешной', 'Депрессивный', 'Экшн', 'Молодежный',
                    'Умный', 'Вдохновляющий', 'Романтичный', 'Волнующий',
                    'Атмосферный', 'Грубый', 'Жестокий', 'Пугающий', 'Необычный',
                    'Трогательный', 'Футуристичный', 'Нереальный', 'Красивый',
                    'Отвратительный', 'Реалистичный', 'Сексуальный']


class Emotion:
    def __init__(self, id):
        self.id = id
        self.name = emotions_names[id]
        self.name_ru = emotions_names_ru[id]


emotions = [Emotion(i) for i in range(len(emotions_names))]
emotions.pop(19)


@app.route('/')
def index():
    return render_template('index.html', emotions=emotions)


@app.route('/search')
def search():
    return 'Search'


if __name__ == '__main__':
    app.run()