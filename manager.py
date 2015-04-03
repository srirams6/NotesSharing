#!/usr/bin/env python
from flask.ext.script import Manager , Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand
from app import app,db,models

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('runserver',Server(port=5000))
manager.add_command('shell',Shell())

@manager.command
def create_db():
        db.create_all()
        depts = ['CSE', 'ECE', 'MECH', 'PROD', 'ICE', 'META', 'CIVIL', 'ARCHI', 'CHEM']
        for dept in depts :
                entry = models.Department(department = dept)
                db.session.add(entry)
                db.session.commit()

manager.add_command('db', MigrateCommand)

@manager.command
def delete_db():
        db.drop_all()

@manager.command
def upgrade_db():
        pass

manager.run()