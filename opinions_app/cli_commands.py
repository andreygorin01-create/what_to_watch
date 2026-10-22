# what_to_watch/opinions_app/cli_commands.py

import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Opinion(
                title=row['title'],
                text=row['text'],
                source=row.get('source') or None,
                added_by=row.get('added_by') or None
            )
            db.session.add(opinion)
            counter += 1
        db.session.commit()
    click.echo(f'Загружено мнений: {counter}')