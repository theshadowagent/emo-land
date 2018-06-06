import tmdbsimple as tmdb

tmdb.API_KEY = '0aaccd7f02b3cf47166614d45183390b'


class Emotion:
    def __init__(self, id):
        self.id = id
        self.name = emotions_names[id]
        self.name_ru = emotions_names_ru[id]


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

emotions = [Emotion(i) for i in range(len(emotions_names))]

movies = [
    {
      "genres": [
        "Action",
        "Comedy",
        "Science Fiction"
      ],
      "id": 383498,
      "image_link": "http://image.tmdb.org/t/p/original/3P52oz9HPQWxcwHOwxtyrVV1LKi.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/to0spRl1CMDvyUbOnbb4fTk3VAd.jpg",
      "rating": 8.0,
      "tagline": "Prepare for the Second Coming.",
      "title": "Deadpool 2",
      "trailer_link": "http://www.youtube.com/watch?v=D86RtevtfrA",
      "year": "2018"
    },
    {
      "genres": [
        "Adventure",
        "Science Fiction",
        "Fantasy",
        "Action"
      ],
      "id": 299536,
      "image_link": "http://image.tmdb.org/t/p/original/bOGkgRGdhrBYJSLpXaxhXVstddV.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
      "rating": 8.5,
      "tagline": "An entire universe. Once and for all.",
      "title": "Avengers: Infinity War",
      "trailer_link": "http://www.youtube.com/watch?v=6ZfuNTqbHE8",
      "year": "2018"
    },
    {
      "genres": [
        "Drama",
        "Romance"
      ],
      "id": 337167,
      "image_link": "http://image.tmdb.org/t/p/original/9ywA15OAiwjSTvg3cBs9B7kOCBF.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/jjPJ4s3DWZZvI4vw8Xfi4Vqa1Q8.jpg",
      "rating": 6.0,
      "tagline": "Don't miss the climax",
      "title": "Fifty Shades Freed",
      "trailer_link": "http://www.youtube.com/watch?v=nJCc5HRPxYA",
      "year": "2018"
    },
    {
      "genres": [
        "Action",
        "Adventure",
        "Fantasy",
        "Science Fiction",
        "Comedy"
      ],
      "id": 284053,
      "image_link": "http://image.tmdb.org/t/p/original/kaIfm5ryEOwYg8mLbq8HkPuM1Fo.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg",
      "rating": 7.4,
      "tagline": "No Hammer. No Problem.",
      "title": "Thor: Ragnarok",
      "trailer_link": "http://www.youtube.com/watch?v=ue80QwXMRHg",
      "year": "2017"
    },
    {
      "genres": [
        "Action",
        "Adventure",
        "Fantasy",
        "Science Fiction"
      ],
      "id": 284054,
      "image_link": "http://image.tmdb.org/t/p/original/AlFqBwJnokrp9zWTXOUv7uhkaeq.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
      "rating": 7.3,
      "tagline": "Long live the king",
      "title": "Black Panther",
      "trailer_link": "http://www.youtube.com/watch?v=xjDjIWPwcPU",
      "year": "2018"
    },
    {
      "genres": [
        "Drama",
        "Romance"
      ],
      "id": 499772,
      "image_link": "http://image.tmdb.org/t/p/original/7tvwYJPostpjFybjOeygnBHVxrW.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/kZJEQFk6eiZ9X2x70ve6R1dczus.jpg",
      "rating": 5.2,
      "tagline": "",
      "title": "Meet Me In St. Gallen",
      "trailer_link": "http://www.youtube.com/watch?v=hBXlOQtrp5k",
      "year": "2018"
    },
    {
      "genres": [
        "Animation",
        "Adventure",
        "Family",
        "Comedy"
      ],
      "id": 269149,
      "image_link": "http://image.tmdb.org/t/p/original/mhdeE1yShHTaDbJVdWyTlzFvNkr.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg",
      "rating": 7.7,
      "tagline": "Welcome to the urban jungle.",
      "title": "Zootopia",
      "trailer_link": "http://www.youtube.com/watch?v=jWM0ct-OLsM",
      "year": "2016"
    },
    {
      "genres": [
        "Action",
        "Science Fiction",
        "Adventure"
      ],
      "id": 118340,
      "image_link": "http://image.tmdb.org/t/p/original/bHarw8xrmQeqf3t8HpuMY7zoK4x.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/y31QB9kn3XSudA15tV7UWQ9XLuW.jpg",
      "rating": 7.9,
      "tagline": "All heroes start somewhere.",
      "title": "Guardians of the Galaxy",
      "trailer_link": "http://www.youtube.com/watch?v=b7yOuhI1dzU",
      "year": "2014"
    },
    {
      "genres": [
        "Action",
        "Adventure",
        "Science Fiction"
      ],
      "id": 348350,
      "image_link": "http://image.tmdb.org/t/p/original/96B1qMN9RxrAFu6uikwFhQ6N6J9.jpg",
      "poster_link": "http://image.tmdb.org/t/p/w600_and_h900_bestv2/3IGbjc5ZC5yxim5W0sFING2kdcz.jpg",
      "rating": 6.9,
      "tagline": "Never tell him the odds.",
      "title": "Solo: A Star Wars Story",
      "trailer_link": "http://www.youtube.com/watch?v=jPEYpryMp2s",
      "year": "2018"
    }
  ]