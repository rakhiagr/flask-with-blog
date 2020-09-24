import click

from flaskblog import db
from flaskblog.models import Post, User

@click.command(name='create_tables')
def create_tables():
    db.create_all()