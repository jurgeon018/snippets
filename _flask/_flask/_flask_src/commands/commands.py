from flask.cli import AppGroup
import click

from app import db
from models import Template


user_cli = AppGroup('user')


@user_cli.command('gen_templates')
@click.argument('name', required=False)
def gen_templates(name):
    print(name)
    for i in range(10):
        templates = Template.query.filter(Template.name==name)
        print(templates)
        # if templates:
        #     template = templates.first()
        # else:
        #     template = Template(name=name)
        #     db.session.add(template)
        #     db.session.commit()
