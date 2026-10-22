### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/andreygorin01-create/what_to_watch.git
cd what_to_watch
```

Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate
```

или для Windows:

```bash
source venv/Scripts/activate
```

Установить зависимости:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Создать файл `.env` в корне проекта (образец в `.env.example`):

```
FLASK_APP=opinions_app
FLASK_DEBUG=1
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
```

Применить миграции и загрузить мнения:

```bash
flask db upgrade
flask load_opinions
```

Запустить проект:

```bash
flask run
```
