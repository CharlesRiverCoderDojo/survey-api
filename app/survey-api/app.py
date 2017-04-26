from chalice import Chalice
from peewee import *

app = Chalice(app_name='survey-api')
db = PostgresqlDatabase('survey', user='root', password='vagrant', host='127.0.0.1')


class BaseModel(Model):
    class Meta:
        database = db

class User(Model):
    username = CharField(unique=True)
    firstname = CharField()
    lastname = CharField()

class Survey(Model):
    user = ForeignKeyField(User, related_name="surveys")
    age = IntegerField()
    grade = IntegerField()
    location = CharField()
    siblings = IntegerField()
    parents = TextField()
    created_date = DateTimeField()

@app.route('/')
def index():
    username = "Person"
    firstname = "Andrea"
    lastname = "Santarlasci"
    return {'username': username,
            'firstname': firstname,
            'lastname': lastname}

# Create a new user
# @app.route('/users', methods=['POST'])
# def create_user():

# Create a new survey
# @app.route('/surveys', methods=['POST'])
# def create_survey():
